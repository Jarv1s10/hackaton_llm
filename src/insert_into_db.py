import os
import re
import json
from typing import Optional
import requests
import asyncio

from bs4 import BeautifulSoup
import yaml

import tiktoken
import weaviate

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from dotenv import load_dotenv
from tqdm import tqdm
from tqdm.asyncio import tqdm_asyncio
import aiohttp

load_dotenv()


def flatten_list(lst: list):
    return [it for sublst in lst for it in sublst]

def delete_html_tags_regex(text):
    tag_regex = re.compile(r'<.*?>')
    t = re.sub(tag_regex, ' ', text)
    t = ' '.join([s for s in t.split(' ') if s])
    return t

def delete_redundant_newlines(text: str):
    return '\n'.join([s.strip() for s in text.split('\n') if s.strip()])

def delete_unicode(text: str):
    return text.encode('ascii', 'ignore').decode()

def delete_useless_text(text: str):
    t = re.sub(r">>> Click to see .*? <<<", '', text)
    t = re.sub(r"\d+ min read(?: - updated few hours ago)?", '', t)
    t = t.replace('For users of the Email Sidebar on:', '')
    return t

def get_clean_text_from_html(html_text: str):
    text = BeautifulSoup(html_text, features="lxml").get_text()
    text = delete_unicode(text)
    text = delete_useless_text(text)
    text = delete_redundant_newlines(text)
    return text

def token_length(text: str, tokenizer: tiktoken.Encoding):
    return len(tokenizer.encode(text))

def get_splitter_len_func(tokenizer: Optional[tiktoken.Encoding] = None):
    if tokenizer is None:
        tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')
    return lambda text: token_length(get_clean_text_from_html(text), tokenizer)

def create_splitter(chunk_size):
    tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')
    len_func = lambda text: token_length(get_clean_text_from_html(text), tokenizer)

    return RecursiveCharacterTextSplitter(["<h1", "<h2", "<h3", "<h4", "<h5", "<h6"],
                                          chunk_size=chunk_size, chunk_overlap=0,
                                          length_function=len_func, keep_separator=True)

def split_html_by_subsections(html_text: str, chunk_size: int):
    splitter = create_splitter(chunk_size)
    splits = splitter._merge_splits(splitter.split_text(html_text), '\n')
    return [get_clean_text_from_html(split) for split in splits]

async def get_article_soup_from_url(http_session: aiohttp.ClientSession, url: str):
    async with http_session.get(url) as r:
        if r.status == 200:
            text = await r.text()
            await asyncio.sleep(2)
            return BeautifulSoup(text, features="lxml").find('article')

async def process_doc_page(http_session: aiohttp.ClientSession, page_url: str, chunk_size: int = 500) -> list[dict]:
    soup = await get_article_soup_from_url(http_session, page_url)

    if soup is None:
        print(f'Article does not exist')
        return []

    doc_html_text = soup.prettify()
    doc_title = soup.find('h1').text

    sections_content = split_html_by_subsections(doc_html_text, chunk_size)
    metadata = {'doc_title': doc_title, 'doc_url': page_url}
    return [{
        'page_content': cont,
        'metadata': metadata
    } for cont in sections_content]

def get_web_path_form_nav(base_url: str, nav_filepath: str):
    if nav_filepath.split('/')[-1].startswith('index'):
        return os.path.join(base_url, os.path.split(nav_filepath)[0])
    return os.path.join(base_url, nav_filepath).replace('.md', '')

def read_mkdocs(mkdocs_filepath: str):
    with open(mkdocs_filepath, 'r') as f:
        try:
            docs_struct = yaml.safe_load(f)
            return docs_struct
        except yaml.YAMLError as e:
            print(e)

def traverse_nav(nav, path=None):
    if path is None:
        path = []

    if isinstance(nav, dict):
        for key, val in nav.items():
            key = delete_html_tags_regex(key)
            if isinstance(val, str):
                yield path, key, val
            else:
                yield from traverse_nav(val, path+[key])

    elif isinstance(nav, list):
        for it in nav:
            yield from traverse_nav(it, path)

async def get_documents(mkdocs_filepath: str) -> list[dict]:
    documents = []
    mkdocs = read_mkdocs(mkdocs_filepath)
    nav = mkdocs['nav']

    session_timeout = aiohttp.ClientTimeout(total=60, sock_connect=30, sock_read=30)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    connector = aiohttp.TCPConnector(limit=20, keepalive_timeout=10)
    async with aiohttp.ClientSession(
        trust_env=True,
        timeout=session_timeout,
        headers=headers,
        connector=connector
    ) as session:
        fs = []
        for _, _, nav_filepath in tqdm(list(traverse_nav(nav))):
            doc_url = get_web_path_form_nav(mkdocs['site_url'], nav_filepath)
            fs.append(process_doc_page(session, doc_url))
        documents = await tqdm_asyncio.gather(*fs)
        documents = flatten_list(documents)

    return documents


async def main():
    mkdocs_filepath = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'sfcc_mkdocs.yml')

    docs_filepath = os.path.join(os.path.dirname(__file__), os.pardir, 'data', 'documents.json')
    if os.path.exists(docs_filepath):
        with open(docs_filepath) as f:
            docs = json.load(f)
    else:
        docs = await get_documents(mkdocs_filepath)
        with open(docs_filepath, 'w') as f:
            json.dump(f, indent=4)

    docs = [Document(**d) for d in docs if d['page_content']]
    print(docs)

    client = weaviate.Client(
        url=os.getenv('WEAVIATE_URL'),
        auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv('WEAVIATE_API_KEY'))
    )

    embeddings = OpenAIEmbeddings()
    Weaviate.from_documents(docs, embeddings, client=client, index_name='RGDocs', by_text=False)

if __name__ == '__main__':
    asyncio.run(main())