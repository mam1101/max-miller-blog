from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os
from pathlib import Path

BUILD_DIRECTORY = './web/'

site_config_dict = ""

with open('site-config.json') as json_file:
    site_config_dict = json.load(json_file)

pages = site_config_dict['pages']

env = Environment(
    loader= FileSystemLoader(searchpath="."),
    autoescape=select_autoescape()
)

for page in pages:
    template_page = page["template"] or "tempaltes/main.html"
    template = env.get_template(template_page)

    path = f'{BUILD_DIRECTORY}{page["path"]}'
    file_path = f'{path}/index.html'
    
    vars = page['vars']

    # create patch and render file
    Path(path).mkdir(parents=True, exist_ok=True)
    
    if not os.path.exists(file_path):
        open(file_path, 'x')

    rendered_page = template.stream(vars).dump(file_path)