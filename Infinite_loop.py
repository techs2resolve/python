import os

while True:
    dirlocation = input("In which directory you want search:- ")
    print(f"Your directory is {dirlocation}")
    print(100 * "=")
    print(f"Going inside the directory {os.chdir(dirlocation)}")
    print(f"Your current working directory is {os.getcwd()}")
    #print(os.listdir(dirlocation))
    filename = input("Enter your filename to search:- ")
    #print(filename)
    if filename in os.listdir(dirlocation):
        print(f"Your file is here {os.getcwd()}/{filename}")
        print(100 * "=")
    else:
        print("Your file not found")
