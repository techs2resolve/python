import os
import fnmatch

for file in os.listdir():
    if fnmatch.fnmatch(file, '*.png'):
        print(file)