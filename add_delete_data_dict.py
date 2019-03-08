# add and delete data in dictonaries


user_info = {
    'name' : 'sarfaraz',
    'age' : 29,
    'fav_movies' : ['sci-fi', 'magic'],
    'fav_songs' : ['terminator', 'lolipop']
}

# Adding data to dict
# for example below we have added a new key : value list in user_info dictonary

user_info['fav_tunes'] = ['song1', 'song2']
print(user_info)

# pop method for removing data
# in the round bracket we have defined the key 'fav_tunes' . It should not be empty. At least we have to define one value

popped_item = user_info.pop('fav_tunes')

print(user_info)
print(popped_item)

# popitem method will randomly delete any key value pair from dict. Most probably the last key value pair from dict.
popped_item = user_info.popitem()
print(user_info)
print(popped_item)