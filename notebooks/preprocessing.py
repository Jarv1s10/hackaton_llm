from genericpath import isfile
import re
import os
import json
from io import StringIO

import yaml
from markdown import Markdown
from tqdm import tqdm


def unmark_element(element, stream=None):
    if stream is None:
        stream = StringIO()
    if element.text:
        stream.write(element.text)
    for sub in element:
        unmark_element(sub, stream)
    if element.tail:
        stream.write(element.tail)
    return stream.getvalue()


# patching Markdown
Markdown.output_formats["plain"] = unmark_element
__md = Markdown(output_format="plain")
__md.stripTopLevelTags = False

HTML_TAG = re.compile(r'<.*?>')


def unmark(text):
    return __md.convert(text).replace('&nbsp;', '\n')


def delete_html_tags(text):
    if '<' not in text:
        return text

    t = re.sub(HTML_TAG, ' ', text)
    t = ' '.join([s for s in t.split(' ') if s])
    return t


def clear_text(text):
    t = unmark(text)
    t = delete_html_tags(t)
    t = '\n'.join([s for s in t.split('\n') if s])
    return t


def get_web_url(base_url: str, nav_filepath: str):
    if nav_filepath.split('/')[-1].startswith('index'):
        return os.path.join(base_url, os.path.split(nav_filepath)[0])
    return os.path.join(base_url, nav_filepath).replace('.md', '')


def read_mkdocs(base_docs: str):
    with open(os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files', base_docs, 'mkdocs.yml'), 'r') as f:
        try:
            docs_struct = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(e)
    return docs_struct


def read_md_file(base_docs: str, nav_filepath: str):
    full_filepath = os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files', base_docs, nav_filepath)
    if not os.path.isfile(full_filepath):
        return

    with open(full_filepath, 'r') as f:
        return f.read()


def traverse_nav(nav, path=None):
    if path is None:
        path = []

    if isinstance(nav, dict):
        for key, val in nav.items():
            key = delete_html_tags(key)
            if isinstance(val, str):
                yield path, key, val
            else:
                yield from traverse_nav(val, path+[key])

    elif isinstance(nav, list):
        for it in nav:
            yield from traverse_nav(it, path)


def preprocess():
    docs_objects = []
    for base_docs in os.listdir(os.path.join(os.path.dirname(__file__), os.pardir, 'markdown_files')):
        mkdocs = read_mkdocs(base_docs)
        nav = mkdocs['nav']

        for nav_keys_path, title, nav_filepath in traverse_nav(nav):
            text = read_md_file(base_docs, nav_filepath)
            if text is None:
                print(f'Markdown file {nav_filepath} referenced in navigation does not exist')
                continue

            clean_text = clear_text(text)

            url = get_web_url(mkdocs['site_url'], nav_filepath)
            site_name = mkdocs['site_name']
            short_site_name = 'C4C' if 'c4c' in base_docs else 'Sfcc'

            doc_obj = {
                'title': title,
                'site_name': site_name,
                'short_site_name': short_site_name,
                'doc_url': url,
                'doc_filepath': nav_filepath,
                'nav_keys_list': nav_keys_path,
                'full_content': text,
                'text_content': clean_text,
            }
            docs_objects.append(doc_obj)
    return docs_objects

if __name__ == '__main__':
    docs_objects = preprocess()
    with open(os.path.join(os.path.dirname(__file__), os.pardir, 'basic_preprocessing', 'docs_objects.json'), 'w') as f:
        json.dump(docs_objects, f, indent=4)