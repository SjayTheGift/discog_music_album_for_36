from django.core.management.base import BaseCommand
from ...models import Music

import requests


class Command(BaseCommand):
    help = 'Download data from discogs api and save it on database.'

    def add_arguments(self, parser):
        parser.add_argument('key', type=str, help='Indicates the key token for the user.')
        parser.add_argument('secret', type=str, help='Indicates the secret token for the user.')

    def get_data(self, key, secret):
        result_list = {}
        for page in range(1, 4):
            response = requests.get("https://api.discogs.com/database/search?style=ambient&artist=36&"
                                     "secret="+secret+"&key="+key+"&genre=electronic&per_page=100&page="+str(page))
            result_list[str(page)] = response.json()['results']

        return result_list

    def handle(self, *args, **kwargs):
        key = kwargs['key']
        secret = kwargs['secret']
        json_data = self.get_data(key, secret)

        for num in range(1, len(json_data)+1):
            for i in json_data[str(num)]:
                try:
                    Music.objects.create(
                        cover_image=i['cover_image'],
                        artist='36',
                        title=i['title'],
                        label=i['label'][0],
                        year=i['year'],
                        catalogue_number=i['catno']
                    )
                except KeyError:
                    Music.objects.create(
                        cover_image=i['cover_image'],
                        artist='36',
                        title=i['title'],
                        label=i['label'][0],
                        year='2019',
                        catalogue_number=i['catno']
                    )
