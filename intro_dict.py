# What are dictonaries
# An unordered collection of data in key : value pair.

# HOW TO CREATE A DICTONARIES :-

user = {
    'name' : 'sarfaraz',
    'age' : 29
}
print(user)

# Second method to create dict :-

user1 = dict(name = 'sarfaraz', age = 29) # you will have to define 'dict' with round brackets.
print(user1)

# How to access data from dictonaries.
# NOTE :- There is no indexing because unordered collections of data.

print(user['name'])
print(user['age'])

#  Which type of data can we store in dictonaries.
# You can store anything like :-  numbers, list, string, dictonaries.

user_info = {
    'name' : 'sarfaraz',
    'age' : 29,
    'fav_movies' : ['sci-fi', 'magic'],
    'fav_songs' : ['terminator', 'lolipop']
}

print(user_info['fav_movies'])


# How to add data in Empty dictonaries:-

user_info2 ={}
user_info2['name'] = 'sarfaraz'
user_info2['age'] = 29
print(user_info2)
