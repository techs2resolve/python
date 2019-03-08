# Word reverse matching using is_palindrom function

def is_palindrom(word):
    return word == word[::-1]

print(is_palindrom("naman"))  # Here the word remain same if you read from right or left. This is called palindrom word.
print(is_palindrom("madam"))
print(is_palindrom("horse"))