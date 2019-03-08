def greatest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

num1 = int(input("Enter the first number:- "))
num2 = int(input("Enter the Second number:- "))
num3 = int(input("Enter the third number:- "))

biggest = greatest(num1, num2, num3)
print(biggest)