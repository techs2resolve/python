
# fromkey method in dict.

d = dict.fromkeys(['name', 'age'], 'unknown')
print(d)

# you can also use this method to get the output in list.
# d = dict.fromkeys(['name', 'age'], ['unknown'])
# print(d)


# get method in dictonaries.
# Below command will give you the value of name key.

print(d.get('name'))

# If the key not found in dict then it will return None
# If you want to print something else instead of None then check below :-

print(d.get('names', 'not found'))

# If you have the same key in the dict then last key will be printed. for e.g.

d = {
    'name' : 'sarfaraz',
    'age' : 29,
    'age' : 30    # This entry will be printed because it take last entry in the same key.
}

print(d)

# You can also use if method in dict.

if 'name' in d:
    print('present')
else:
    print('not present')


# Second method of if condition in dict.

if d.get('name'):
    print('present')
else:
    print('not present')


# If you want to clear your dict check the below command.

# d.clear()
# print(d)

# How to make a copy of the dictonaries.
# We have copied the data in d1 dictonaries from d.

d1 = d.copy()
print(d1)

