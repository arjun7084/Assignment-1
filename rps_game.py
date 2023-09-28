import random

user_input = input("Enter your choice [Rock, Paper, Scissors]: ")
computer_choice = ["Rock", "Paper", "Scissors"]
computer_input = random.choice(computer_choice)

print(user_input)
print(computer_input)