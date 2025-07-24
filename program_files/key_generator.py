from faker import Faker
from random import randint
import re
import os


DEFAULT_KEYS = ['from', 'lost', 'deliver', 'song', 'listen']


def generate_keys(quantity=0) -> list:
    quantity = quantity if quantity != 0 else randint(1,10)
    fake = Faker('en_US')
    return (fake.words(nb=quantity))


def read_keys(src_path: str) -> list:
    keys = []
    try:
        with open(src_path, 'r', encoding='UTF-8') as f:
            for line in f:
                parts = re.split(r'[ ,.:;()\[\]{}?!\"\\/|]+', line)
                clean_parts = [part.strip().strip(',.:;()[]{\|/}?!\'\"') for part in parts if part]
                keys.extend([part for part in clean_parts if part])
            return keys
    except FileNotFoundError as e:
        print(f'File {src_path} not found: {e}')
        return []
    except IOError as e:
        print(f'File can`t be written: {e}')
        return []


def get_path()-> str:
    while True:
        src_path = input("Enter path to file with keywords: ").strip()
        if os.path.exists(src_path) and os.path.isfile(src_path):
            return src_path
        else:
            print(f'Entered path - {src_path} - not found or not a file.')


def get_keys() -> list:
    choice = input(f"If you want to generate random keys for search - enter 'G(enerate)' or 'g(enerate)', if you want to read keys from file - enter 'R(ead)' or 'r(ead)'; otherwise will be used predefined list of keys: {DEFAULT_KEYS}. \n\n Enter your choice here: ")
    match choice.strip().lower():
        case 'g' | 'generate':
            return generate_keys()
        case 'r' | 'read':
            src_path = get_path()
            current = read_keys(src_path)
            return current if len(current) != 0 else DEFAULT_KEYS
        case _:
            return DEFAULT_KEYS

if __name__ == '__main__':
    result = get_keys()
    print(result)