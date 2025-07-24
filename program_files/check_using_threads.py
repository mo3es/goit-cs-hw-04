import concurrent.futures
import os
from . import handle_path_to_texts as hpt
from .check_on_keys_presents import Checker
from .key_generator import get_keys


def implement_environments(path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/texts'))
) -> (list, list):
    key_list = get_keys()
    path_list = hpt.path_processing(path)
    return (key_list, path_list)

def get_max_workers():
    workers = input("Enter number of treads, that you'd like to use (from 2 to 12, otherwise will be set by default): ")
    if workers.isnumeric():
        workers = int(workers)
    return workers if workers in range(2, 12) else 2


def check_files(path=None):
    key_list, path_list = implement_environments(path)
    workers = get_max_workers()
    checker = Checker()
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(checker.check_file, path, key_list): path for path in path_list}
        for future in concurrent.futures.as_completed(futures):
            path_item = futures[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                print(f'An exception occured while {path_item} processed')
                results.append({os.path.basename(path_item) : {"error": str(e)}})
    return results


if __name__ == '__main__':
    results = check_files()
    print(results)