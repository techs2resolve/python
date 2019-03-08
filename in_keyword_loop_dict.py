

user_info = {
    'name' : 'sarfaraz',
    'age' : 29,
    'fav_movies' : ['sci-fi', 'magic'],
    'fav_songs' : ['terminator', 'lolipop']
}

# How to check the key exist in dict:-

if 'name' in user_info:
    print('present')
else:
    print('not present')

# How to check Value exist in dict:-

if 'sarfaraz' in user_info.values():
    print('present')
else:
    print('not present')

#  How to run loop inside dict:-
# # To print only keys in dict :-
#
# for i in user_info:
#     print(i)
#
# # To print values only in dict:-
# for i in user_info.values():
#     print(i)

# To print values without for loop using values method.

# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values)) # checking data type.
#
# # To print the keys without for loop using keys method.
#
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))
#
#
# # forloop to get values :-
#
# for i in user_info:
#     print(user_info[i])

# ITEM METHOD IN DICT:-

user_info_items = user_info.items()
print(user_info_items)
print(type(user_info_items))


for key, value in user_info.items():
    print(f"key is {key} and value is {value}")

