import concurrent.futures
import os
from .check_on_keys_presents import Checker
from .check_using_threads import get_max_workers, implement_environments



def check(path):
    key_list, path_list = implement_environments(path)
    workers = get_max_workers()
    checker = Checker()
    results = []
    with concurrent.futures.ProcessPoolExecutor(max_workers=workers) as executor:
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
    results = check()
    print(results)