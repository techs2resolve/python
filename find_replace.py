import os
#Replace method
# Replacing space with _ underscore

name = "My name is Sarfaraz Shaikh. This is working "
print(name.replace(" ", "_"))

# Replacing any word like is to was

print(name.replace("is", "was"))

# If you want to replace only first is with was do like below You will have do define the position number to start finding

print(name.replace("is", "was", 1))

# Find Method

print(name.find("is"))
