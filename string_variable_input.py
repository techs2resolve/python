

# one = int(input("Enter your First number:- "))
# two = int(input("Enter your Second number:- "))
# three = int(input("Enter your Third number:- "))
#
# total = one + two + three
# print(f"Your total is {total}")
# average = total / 3
# print("Your average is :- " + str(average))

num1,num2,num3 = input("Enter number one by one three time separated by comas ").split(",")
print(f"Your first number is {num1} and Your second number is {num2} and your third number is {num3}")

total = int(num1) + int(num2) + int(num3)
totals =
average = total / 3
print("Average of 3 numbers is :- " + str(average))
