import pathlib
from enum import Enum
from typing import Union

import yaml


class NetlifyCMSWidget(Enum):
    Boolean = 0
    DateTime = 1
    File = 2
    Hidden = 3
    Image = 4
    List = 5
    Map = 6
    Markdown = 7
    Number = 8
    Object = 9
    Relation = 10
    Select = 11
    String = 12
    Text = 13


class NetlifyCMS(object):
    def __init__(self, output_directory: Union[str, pathlib.Path] = pathlib.Path('build/admin'),
                 publish_mode='editorial_workflow', media_folder='/src/images', public_folder='/images',
                 branch='master'):
        if not isinstance(output_directory, pathlib.Path):
            output_directory = pathlib.Path(output_directory)

        self.output_directory = output_directory
        self.dictionary = {
            'publish_mode': publish_mode,
            'media_folder': media_folder,
            'public_folder': public_folder,
            'backend': {
                'name': 'git-gateway',
                'branch': branch
            },
            'collections': []
        }

    def add_collection(self, name, label, folder, create: bool, slug):
        self.dictionary['collections'].append({
            'name': name,
            'label': label,
            'folder': folder,
            'create': create,
            'slug': slug,
            'fields': []
        })

    def add_widget(self, collection: str, widget, name, label, default, **kwargs):
        try:
            collection_index = next((i for i, x in enumerate(self.dictionary['collections'])))
        except StopIteration:
            raise KeyError(
                'That collection does not exist. Please create the collection {} before using it.'.format(collection))

        self.dictionary['collections'][collection_index]['fields'].append(
            self.widget2dict(widget, name, label, default, **kwargs))

    @staticmethod
    def widget2dict(widget, name, label, default, **kwargs) -> dict:
        if widget == NetlifyCMSWidget.Boolean:
            return {'widget': 'boolean', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.DateTime:
            return {'widget': 'datetime', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.File:
            return {'widget': 'file', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Hidden:
            return {'widget': 'hidden', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Image:
            return {'widget': 'image', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.List:
            return {'widget': 'list', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Map:
            return {'widget': 'map', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Markdown:
            return {'widget': 'markdown', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Number:
            return {'widget': 'number', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Object:
            return {'widget': 'object', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Relation:
            return {'widget': 'relation', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Select:
            return {'widget': 'select', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.String:
            return {'widget': 'string', 'name': name, 'label': label, 'default': default, **kwargs}
        elif widget == NetlifyCMSWidget.Text:
            return {'widget': 'text', 'name': name, 'label': label, 'default': default, **kwargs}

    def save(self):
        with self.output_directory.joinpath('index.html').open(mode='w+') as f:
            f.write("""
            <!doctype html>
            <html>
            <head>
              <meta charset="utf-8" />
              <meta name="viewport" content="width=device-width, initial-scale=1.0" />
              <title>Content Manager</title>
            </head>
            <body>
              <!-- Include the script that builds the page and powers Netlify CMS -->
              <script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script>
            </body>
            </html>
            """)

        with self.output_directory.joinpath('config.yml').open(mode='w+') as f:
            yaml.dump(self.dictionary, f)
