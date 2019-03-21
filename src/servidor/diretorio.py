
import os


def info_diretorios(path=os.path.expanduser('~')):
    directories_files = {}
    for path, sub_dir, files in os.walk(os.path.abspath(path)):
        directories_files[path] = [sub_dir, files]

    for key, value in directories_files.items():
        print(key, value)
