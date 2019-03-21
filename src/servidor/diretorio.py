
import os


def info_diretorios(path):
    directories_files = {}
    for path, sub_dir, files in os.walk(os.path.abspath(path)):
        directories_files[path] = [sub_dir, files]

    for key, value in directories_files.items():
        print(key, value)


# files_path04('C:\\Users\\user1\\Desktop\\')
info_diretorios(
    f"""{os.path.expanduser('~')}/Projects/infnet/PB_Arq_Infnet/src""")
