# Set data type
# unordered collection of unique items.

# You cannot store dict and list inside sets.
# You can store int, float and string.

#  curly braces is used to create sets.
# It will not count the same data, for e.g if you have two similar entry then it will display only one.
# You cannot do indexing in sets.

s = {1,2,3}
# print(s)   # it will not print the same data like '2' in the sets.
#
#
# # How to remove duplicate items from the list
# # This is the most important use of sets
#
# l = [1,2,2,3,3,3,3,4,4,4,5,5,5,5,6,6]
# s2 = set(l)
# print(s2)
#
# # Then again convert back to list.
#
# s2 = list(set(l))
# print(s2)

# # How to add data in sets.
# s.add(4)
# print(s)

# How to remove data from sets.
# s.remove(2)
# print(s)

# Discard method wont give any error if the value is not present.
# s.discard(3)
# print(s)

# To clear the set
# s.clear()
# print(s)

s1 = s.copy()
print(s1)



