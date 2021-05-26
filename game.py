# game.py

import random
import os

PLAYER_NAME = os.getenv("PLAYER_NAME", default = "Player One")

print("--------------------------------------------------")

print(f"Hi {PLAYER_NAME} Let's Play a Game:")

print("Rock, Paper, Scissors, Shoot!")

print("--------------------------------------------------")

user_choice = input("You go first! Choose an action 'rock','paper','scissors':")

#print(user_choice)
print("You Chose: ", user_choice)

#validate the input such that only if it is one of the expected values
#... will we continue with the rest of the program
#... otherwise we'll stop the program before it tries to do anything else
#... and we'll ask the user to run the program again

if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("--------------------------------------------------")

else:
    print("OOPS, invalid input.  Please try again.")
    exit()

valid_options = ["rock","paper","scissors"]
computer_choice = random.choice(valid_options)

print("Computer Chose: ",computer_choice)

print("--------------------------------------------------")

print("Game Result:")

if (user_choice == computer_choice):
    print("Tie!")
elif ((user_choice == "rock") and (computer_choice == "scissors")):
    print("You win!")
elif ((user_choice == "paper") and (computer_choice == "rock")):
    print("You win!")
elif ((user_choice == "scissors") and (computer_choice == "paper")):
    print("You Win!")
elif ((computer_choice == "rock") and (user_choice == "scissors")):
    print("Computer Wins. Try again!")
elif ((computer_choice == "paper") and (user_choice == "rock")):
    print("Computer Wins. Try again!")
elif ((computer_choice == "scissors") and (user_choice == "paper")):
    print("Computer Wins. Try again!")
    exit()


print("--------------------------------------------------")

print("Thanks for Playing!")