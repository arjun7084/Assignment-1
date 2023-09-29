import random

user_points = 0
computer_points= 0

while True:
    user_input = input("Enter your choice [Rock, Paper, Scissors]: ")
    computer_choice = ["Rock", "Paper", "Scissors"]
    computer_input = random.choice(computer_choice)

    print(f"You chose - {user_input} \nComputer chose - {computer_input}")


    if user_input == computer_input:
        print(f"It is a tie! because you both chose: {user_input}")
    elif user_input == "Rock":
        if computer_input == "Scissors":
            print("User wins, Rock will break the scissors.")
            user_points += 1
        else:
            print("User lose, Paper will cover the rock.")
            computer_points += 1


    elif user_input == "Paper":
        if computer_input == "Rock":
            print("User wins, Paper will cover the rock.")
            user_points += 1
        else:
            print("User lose, Scissors will cut the paper.")
            computer_points += 1


    elif user_input == "Scissors":
        if computer_input == "Paper":
            print("User wins, Scissors will cut the paper.")
            user_points += 1
        else:
            print("User lose, Rock will break the scissors.")
            computer_points += 1

    play_again = input("\nDo you want to play again ? (y/n): ")
    if play_again.lower() != "y":
        break

print(f"\nTotal points are:- \nUser - {user_points} \nComputer - {computer_points}")
print("\nGame Over!")
