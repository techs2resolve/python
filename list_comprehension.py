

# list comprehension
# with the help of list comprehension we can create list with mininal code.
#
# # old method to create a  list
#
# # Create a list of square from 1 to 10

square = []
for i in range(1,11):
    square.append(i**2)
print(square)
#
# # Now we will use list comprehension method to create a list.
#
square2 = [i**2 for i in range(1,11)]
print(square2)
#
# ##### Second example old method.
#
negative = []
for i in range(1,11):
    negative.append(-i)
print(negative)
#
# ####List comprehension method.
#
new_negative = [-i for i in range(1,11)]
print(new_negative)


##### Third example old method.
#
names = ['Sarfaraz', 'Ali', 'Suleiman']
#
new_list = []

for name in names:
    new_list.append(name[0])

print(new_list)



#### list comprehension method.
#
new_names = [name[0] for name in names]
print(new_names)