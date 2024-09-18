from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os
import sys
from pathlib import Path

BUILD_DIRECTORY = './web/'

JINJA_ENV = Environment(
    loader= FileSystemLoader(searchpath="."),
    autoescape=select_autoescape()
)


site_config_dict = ""

with open('site-config.json') as json_file:
    site_config_dict = json.load(json_file)

PAGES = site_config_dict['pages']

GLOBAL_VARS = site_config_dict['global']

def build_single(name, page):
    template_page = page["template"] or "tempaltes/main.html"
    template = JINJA_ENV.get_template(template_page)

    path = f'{BUILD_DIRECTORY}{page["path"]}'
    file_path = f'{path}/index.html'
    
    vars = page['vars']

    # create patch and render file
    Path(path).mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(file_path):
        open(file_path, 'x')

    build_vars = GLOBAL_VARS
    build_vars.update(vars)
    
    template.stream(build_vars).dump(file_path)

def build_all():
    for name, page in PAGES.items():
        build_single(name, page)


if __name__ == "__main__":
    try:
        page_to_render = sys.argv[1]
        if (page_to_render):
            build_single(page_to_render, PAGES[page_to_render])
    except:
        build_all()