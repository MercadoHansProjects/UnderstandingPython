#GuessTheNumber

import random

secret = random.randint(1, 100)


while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("You got it!")
        break
    elif guess > secret:
        print("Engk, Engot, Lower")
    elif guess < secret:
        print("Engk, Engot, Higher")



