
import os

def files_path04(path):
    for p, _, files in os.walk(os.path.abspath(path)):
        print(p)
        print(_)
        print(files)
        print()
        #for file in files:
            #print(os.path.join(p, file))

files_path04('C:\\Users\\user1\\Desktop\\')