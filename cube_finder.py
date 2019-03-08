

def cube_finder(num1):
    cubes = {}
    for i in range(1,num1+1):
        cubes[i] = i**3
    return cubes

print(cube_finder(10))

# # print(cube_finder(3))
# user_input = int(input('Enter the number :- '))
# print(f"The cube of your number {user_input} is",cube_finder(user_input))
#
# print(['user_input','cube_finder'])
