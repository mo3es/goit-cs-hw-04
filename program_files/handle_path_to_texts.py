import os


def get_path() -> str:
    while True:
        src_path = input("Enter path to file (directory) with text(s): ").strip()
        if os.path.exists(src_path):
            return src_path
        else:
            print(f'Entered path - {src_path} - not found.')


def handle_path(path: str) -> list:
    files = []
    if os.path.isdir(path):
        for file in os.listdir(path):
            if file.lower().endswith(('.txt', '.md', '.log')):
                full_path = os.path.join(path, file)
                files.append(os.path.abspath(full_path)) if os.path.isfile(full_path) else files
    else:
        if path.lower().endswith(('.txt', '.md', '.log')):
            files.append(os.path.abspath(path))
    return files


def path_processing(path: str = None) -> list:
    if not path or not os.path.exists(path):
        path = get_path()
    files = handle_path(path)
    if len(files) == 0:
        print('Given path doesn`t contain text-associated files')
    return files