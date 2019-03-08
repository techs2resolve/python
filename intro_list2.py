

# pop, del, remove

fruit = ["apple", "mango", "banana", "kiwi"]

# fruit.pop()  # By default it will remove the last item in the list if you have not provided the index number
#
# fruit.pop(1) # You can provide the index number here to delete item.
#
# print(fruit)
# print(len(fruit[3]))


# del method
### You can also use del methon to remove the items from the list.

# del fruit[1] #
# print(fruit)

#Remove Method
## You can also use remove method
# Remove method is used when you dont know the index number of the item in the list.

fruit.remove("banana")
print(fruit)
