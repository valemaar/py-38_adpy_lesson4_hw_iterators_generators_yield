# 2. Написать генератор, который принимает путь к файлу.
# При каждой итерации возвращает md5 хеш каждой строки файла.

import hashlib

PATH_TEXT_FILE = 'countries.txt'


def strings_hash(path):
    with open(path, "r", encoding='utf-8') as file:
        for line in file:
            string_hash = hashlib.md5(line.strip().encode()).hexdigest()
            yield string_hash


for string in strings_hash(PATH_TEXT_FILE):
    print(string)
