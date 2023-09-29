import random

while True:
    user_input = input("Enter your choice [Rock, Paper, Scissors]: ")
    computer_choice = ["Rock", "Paper", "Scissors"]
    computer_input = random.choice(computer_choice)

    print(f"You chose {user_input} - Computer chose {computer_input}")


    if user_input == computer_input:
        print(f"It is a tie! {user_input}")
    elif user_input == "Rock":
        if computer_input == "Scissors":
            print("User wins, Rock will break the scissors.")
        else:
            print("User lose, Paper will cover the rock.")


    elif user_input == "Paper":
        if computer_input == "Rock":
            print("User wins, Paper will cover the rock.")
        else:
            print("User lose, Scissors will cut the paper.")

    elif user_input == "Scissors":
        if computer_input == "Paper":
            print("User wins, Scissors will cut the paper..")
        else:
            print("User lose, Rock will break the scissors.")

    play_again = input("Do you want to play again ? (y/n): ")
    if play_again.lower() != "y":
        break

print("Game Over!")
