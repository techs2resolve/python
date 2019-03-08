

# word counter

def word_counter(s):
    count = {}
    for char in s:
        count[char] = s.count(char)
    return count

name = input('Enter your name :- ')
print(word_counter(name))