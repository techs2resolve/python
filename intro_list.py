

# list method for inserting data in the list

#
fruit = ["apple", "grapes"]
fruit.append("mango") # manually appending data into list
print(fruit)

fruit.append(input("Enter the fruit name:- ")) # appending data with the help of user input.
print(fruit)

## List Insert method.
#if you want to insert the data on the particular place then use insert method.

fruit1 = ["pineapple", "strawberry"]
fruit_name = input("Enter the name:- ")
fruit1.insert(0,"Apple")
print(fruit1)

### Adding two list together

total_fruits = fruit + fruit1
print(total_fruits)


### You can also use List extend method to add more data in the list.

fruit.extend(fruit1)
print(fruit)




