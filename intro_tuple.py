mixed = (1,2,3,4.0)

for i in mixed:
    print(i)



# tuple without paranthesis.

guitars = 'yamaha', 'baton rogue', 'taylor'

# tuple unpacking

guitarists = ('Maneli Jamal', 'Eddie ven de meer', 'Andrew Roy')

guitarists1,guitarists2,guitarists3 = (guitarists)

print(guitarists)

# list inside tuple

favourites = ('southern mangole', ['Tokyo Ghoul', 'landscape'])

favourites[1].pop()
print(favourites)
favourites[1].append("We made it")
print(favourites)

