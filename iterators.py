# 1. Написать класс итератора, который по каждой стране
# из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка.
# Ссылку формировать самостоятельно.

import json

PATH_FILE = 'countries.json'


class CountryWikiLinks:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, encoding="utf-8") as f:
            json_data = json.load(f)

        with open('countries.txt', 'w', encoding='utf-8') as f:
            for item in json_data:
                self.countries = item['name']['common']
                self.links = 'https://en.wikipedia.org/wiki/' + str(self.countries).replace(' ', '_')
                yield self.links
                f.write(f'{self.countries} - {self.links}\n')

    def __next__(self):
        link = next(self.links)
        return link


for links in CountryWikiLinks(PATH_FILE):
    pass
