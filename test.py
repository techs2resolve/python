import os
import shutil
import sys

print('This is test script')
print( 100 * '=' )
print('Checking the current working directory')
print('Your current working directory is', os.getcwd())
print('Listing the directory')
#print(os.listdir(os.getcwd()))

for item in os.listdir(os.getcwd()):
    print(item[0:50])

print("\U0001F600")


