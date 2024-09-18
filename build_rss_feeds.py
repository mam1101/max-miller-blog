import rfeed
import json

BASE_DOODLE_URL = 'https://maxmiller.ink/'

with open('site-config.json') as json_file:
    site_config_dict = json.load(json_file)

PAGES = site_config_dict['pages']
_items = []

for name, page in PAGES.items():
    if 'Doodle: ' in name:
        vars = page['vars']
        _items.append(rfeed.Item(
            link = vars['title_doodle'],
            title = f'{BASE_DOODLE_URL}{page["path"]}',
            author = "A Chair in the Void",
            description = vars['img_title_doodle']
        ))

feed = rfeed.Feed(title="ACTV: Doodles",
                  description = "The lastest Doodles from A Chair in the Void",
                  language="en-US",
                  items=_items,
                  link=f'{BASE_DOODLE_URL}doodles/feed/'
)

with open('./web/doodles/feed.xml', 'w') as f:
    f.write(feed.rss())