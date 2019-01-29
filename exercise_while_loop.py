

n = input("Enter the number:- ")

print(len(n))

total = 0
i = 0

while i < len(n):
    total = total + int(n[i])
    i += 1
    print(total)
