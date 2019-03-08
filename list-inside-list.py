


# print list inside list with for loop

matrix = [['1','2','3'], ['4','5','6'],['7','8','9']]

# print(matrix)

# print(matrix[2][1]) # This way you can print the particular content of list inside list. In this example we are
                      # printing the 2nd list first index

# print(len(matrix))

for sublist in matrix:
    for i in sublist:
        print(i)