import re
import requests
from bs4 import BeautifulSoup
import tiktoken

from langchain.text_splitter import RecursiveCharacterTextSplitter


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

def get_splitter_len_func(tokenizer: tiktoken.Encoding = None):
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

def get_article_soup_from_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return BeautifulSoup(r.content.decode(), features="lxml").find('article')

def process_doc_page(page_url: str, chunk_size: int = 500) -> list[dict]:
    soup = get_article_soup_from_url(page_url)
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