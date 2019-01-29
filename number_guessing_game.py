
# We can use fix winning number or we can use randomly generated number with the help of random module.
# We will use random module to automatically generate winning number here.
import random

winning_number = random.randint(1, 100) # we have used random module here
#print(winning_number) To print the winning the number
#winning_number = 43 # First we have used fixed number
guess = 1
game_over = False
number = int(input("Enter a number:- "))

while not game_over:
    if number == winning_number:
        print(f"You win the game, You guess the number in {guess} times")
        game_over = True
    else:
        if number < winning_number:
            print("Too Low")
            guess += 1
            number = int(input("Guess again:- "))
        else:
            if number > winning_number:
                print("Too High")
                guess += 1
                number = int(input("Guess again:- "))