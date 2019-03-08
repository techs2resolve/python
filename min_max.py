numbers = [10,20,50]

print(min(numbers))
print(max(numbers))

def greatest_number(l):
    return max(l) - min(l)


print(greatest_number(numbers))