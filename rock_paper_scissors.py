# Rock Paper Scissors program using Multiple If statements

import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ")

    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors()
