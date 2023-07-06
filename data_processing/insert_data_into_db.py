import os
import re
import json
import requests
import getpass

import yaml
from bs4 import BeautifulSoup
from markdown import Markdown
import tiktoken
import weaviate

from langchain.text_splitter import RecursiveCharacterTextSplitter, TextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate


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

def get_splitter_len_func(tokenizer: tiktoken.Encoding):
    return lambda text: token_length(get_clean_text_from_html(text), tokenizer)

def create_splitter(chunk_size, len_func):
    return RecursiveCharacterTextSplitter(["<h1", "<h2", "<h3", "<h4", "<h5", "<h6"],
                                          chunk_size=chunk_size, chunk_overlap=0,
                                          length_function=len_func, keep_separator=True)

def split_html_by_subsections(html_text: str, splitter: TextSplitter):
    splits = splitter._merge_splits(splitter.split_text(html_text), '\n')
    return list(map(get_clean_text_from_html, splits))

def get_article_soup_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return BeautifulSoup(r.content.decode(), features="lxml").find('article')

def get_web_url_form_nav(base_url: str, nav_filepath: str):
    if nav_filepath.split('/')[-1].startswith('index'):
        return os.path.join(base_url, os.path.split(nav_filepath)[0])
    return os.path.join(base_url, nav_filepath).replace('.md', '')

def read_mkdocs(base_docs: str):
    with open(os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files', base_docs, 'mkdocs.yml'), 'r') as f:
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

def get_sections_documents():
    tokenizer = tiktoken.encoding_for_model('gpt-3.5-turbo')
    splitter = create_splitter(500, get_splitter_len_func(tokenizer))

    documents = []
    for base_docs in os.listdir(os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files')):
        mkdocs = read_mkdocs(base_docs)
        nav = mkdocs['nav']
        for nav_keys_path, doc_title, nav_filepath in traverse_nav(nav):

            doc_url = get_web_url_form_nav(mkdocs['site_url'], nav_filepath)
            doc_soup = get_article_soup_from_url(doc_url)

            if doc_soup is None:
                print(f'Article {doc_title} referenced in navigation does not exist')
                continue

            site_name = mkdocs['site_name']
            short_site_name = 'C4C' if 'c4c' in base_docs else 'Sfcc'

            doc_html_text = doc_soup.prettify()
            sections_content = split_html_by_subsections(doc_html_text, splitter)
            for sec_content in sections_content:
                sec_metadata = {
                    'doc_title': doc_title,
                    'site_name': site_name,
                    'short_site_name': short_site_name,
                    'doc_url': doc_url,
                    'doc_md_filepath': nav_filepath,
                    'doc_navigation_path': ' // '.join(list(map(lambda x: delete_html_tags_regex(x).strip(), nav_keys_path))),
                    'section_token_length': token_length(sec_content, tokenizer)
                }
                documents.append({'page_content': sec_content, 'metadata': sec_metadata})  # lc.schema.Document(page_content=sec_content, metadata=sec_metadata)
    return documents


if __name__ == '__main__':
    docs_path = os.path.join(os.path.dirname(__file__), os.pardir, 'preprocessed_data', 'documents.json')

    if os.path.isfile(docs_path):
        with open(docs_path, 'r') as f:
            docs = json.load(f)
    else:
        sections_docs = get_sections_documents()
        with open(docs_path, 'w') as f:
            json.dump(sections_docs, f, indent=4)

    docs = [Document(**d) for d in docs]


    os.environ['OPENAI_API_KEY'] = getpass.getpass("OpenAI API Key:")
    WEAVIATE_API_KEY = getpass.getpass("Weaviate API Key:")
    WEAVIATE_URL = getpass.getpass("Weaviate URL:")

    client = weaviate.Client(url=WEAVIATE_URL,
                             auth_client_secret=weaviate.AuthApiKey(api_key=WEAVIATE_API_KEY))

    embeddings = OpenAIEmbeddings()
    db = Weaviate.from_documents(docs, embeddings, client=client, index_name='RGDocs', by_text=False)
