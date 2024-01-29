import random

number = random.randint(1, 10)
guess = None

while guess != number:
    guess = input("Guess a number between 1 and 10: ") #gibt als input eine zahl ein
    guess =int(guess)

    if guess == number: # vergleicht den Input mit der random Zahl
        print("Congartulations! You won:)")
        break
    else:
        print("Wrong. Try again!")
        
