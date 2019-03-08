


name, age = input('Enter your name and age separated by commas :- ').split(',')
fav_movies = input("Enter your fav movies :- ").split(',')
fav_songs = input("Enter your fav songs :- ").split(',')

print(f"Your name is {name} and your age is {age}")
print(f"Your fav movies are {fav_movies}")
print(f"Your fav songs are {fav_songs}")

user = {}

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_songs'] = fav_songs
#print(user)

for key, value in user.items():
    print(f"{key} : {value}")
