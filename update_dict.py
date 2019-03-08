# Update method in dict.

user_info = {
    'name' : 'sarfaraz',
    'age' : 29,
    'fav_movies' : ['sci-fi', 'magic'],
    'fav_songs' : ['terminator', 'lolipop']
}


more_info = {
    'name' : 'Sarfaraz Shaikh',
    'state' : 'Gujarat',
    'hobbies' : ['Reading', 'Writing', 'Coding']
}


user_info.update(more_info)
print(user_info)


# for example if you update the exisitng key like name. It will update value with new data. check above