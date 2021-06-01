# 1. Написать класс итератора, который по каждой стране из файла countries.json ищет страницу из википедии.
# Записывает в файл пару: страна – ссылка. Ссылку формировать самостоятельно.

import json

PATH_FILE = 'countries.json'


class CountryWikiLinks:

    def __iter__(self):
        with open(PATH_FILE, encoding="utf-8") as f:
            json_data = json.load(f)
        for item in json_data:
            self.countries = iter([country for country in item['name']['common']])

        return self

    def __next__(self):
        country = next(self.countries)
        yield country.text


for country in CountryWikiLinks():
    print(country)
