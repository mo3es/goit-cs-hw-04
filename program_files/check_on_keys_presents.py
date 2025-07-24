import re
import os

class Checker:

    def __init__(self):
        pass

    def check_file(self, path: str, keys: list) -> dict:
        result = {}
        words = []
        name = os.path.basename(path)
        try:
            with open(path, 'r', encoding='UTF-8') as f:
                for line in f:
                    parts = re.split(r'[ ,.:;()\[\]{}?!\"\\/|]+', line)
                    clean_parts = [part.strip().strip(',.:;()[]{\|/}?!\'\"') for part in parts if part]
                    words.extend([part for part in clean_parts if part])
        except FileNotFoundError as e:
            print(f'File {path} not found: {e}')
            return {name: {}}
        except IOError as e:
            print(f'File can`t be readen: {e}')
            return {name : {}}
        for key in keys:
            key_count = words.count(key)
            result[key] = key_count if key_count else 0
        return {name: result}