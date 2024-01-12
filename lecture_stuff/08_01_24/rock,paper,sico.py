import random

user_action = input("Enter a choice (rock,paper,scissors): ")
possible_actions = ["rock","paper","scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print("Both player selected " + {user_action} + "try again.")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock beats scissors")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
