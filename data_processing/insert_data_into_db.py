import os
import re
import json
import sys

sys.path.append(
    os.path.join(os.path.dirname(__file__), os.pardir)
)

import yaml
import weaviate

from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
from dotenv import load_dotenv

from chatbot.api.process_doc_page import process_doc_page

def delete_html_tags_regex(text):
    tag_regex = re.compile(r'<.*?>')
    t = re.sub(tag_regex, ' ', text)
    t = ' '.join([s for s in t.split(' ') if s])
    return t

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
    documents = []
    for base_docs in os.listdir(os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files')):
        mkdocs = read_mkdocs(base_docs)
        nav = mkdocs['nav']
        for _, _, nav_filepath in traverse_nav(nav):

            doc_url = get_web_url_form_nav(mkdocs['site_url'], nav_filepath)
            documents.extend(process_doc_page(doc_url))

    return documents


if __name__ == '__main__':
    load_dotenv(
        os.path.join(os.path.dirname(__file__), os.pardir, 'chatbot', 'api', '.env')
    )
    docs_path = os.path.join(os.path.dirname(__file__), os.pardir, 'preprocessed_data', 'documents.json')

    if os.path.isfile(docs_path):
        with open(docs_path, 'r') as f:
            docs = json.load(f)
    else:
        sections_docs = get_sections_documents()
        with open(docs_path, 'w') as f:
            json.dump(sections_docs, f, indent=4)

    docs = [Document(**d) for d in docs]

    # os.environ['OPENAI_API_KEY'] = getpass.getpass("OpenAI API Key:")
    # WEAVIATE_API_KEY = getpass.getpass("Weaviate API Key:")
    # WEAVIATE_URL = getpass.getpass("Weaviate URL:")

    client = weaviate.Client(
        url=os.getenv('WEAVIATE_URL'),
        auth_client_secret=weaviate.AuthApiKey(api_key=os.getenv('WEAVIATE_API_KEY'))
    )

    embeddings = OpenAIEmbeddings()
    db = Weaviate.from_documents(docs, embeddings, client=client, index_name='RGDocs', by_text=False)
