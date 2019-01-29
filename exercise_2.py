# name = input('Enter your name :- ')
# print(name[::-1])
# print(len(name))
# print(name.upper())
# print(name.title())

name, char = input('Enter your name and char :- ').split(",")
print(f"The length of your name is {len(name)} character and your age is {char}")
print(name.count(char))

