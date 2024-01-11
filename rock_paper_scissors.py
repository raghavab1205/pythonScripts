import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = input(print("Enter the choice(rock, papers, scissors) : "))
user_choice = 0
user_show = ""
if (user == "rock") or (user == "ROCK") or (user == "Rock"):
    user_choice = 1
elif (user == "papers") or (user == "PAPERS") or (user == "Papers") or (user == "paper") or (user == "PAPER") or (user == "Paper"):
    user_choice = 2
elif (user == "scissors") or (user == "SCISSORS") or (user == "Scissors") or (user == "scissor") or (user == "SCISSOR") or (user == "Scissor"):
    user_choice = 3

print("You have chose : ")
if user_choice == 1:
    user_show = rock
    print(rock)
elif user_choice == 2:
    user_show = paper
    print(paper)
elif user_choice == 3:
    user_show = scissors
    print(scissors)

print("The computer has chosen : ")
comp_choice = random.randint(1, 3)
comp_show = ""
if comp_choice == 1:
    comp_show = rock
    print(rock)
elif comp_choice == 2:
    comp_show = paper
    print(paper)
elif comp_choice == 3:
    comp_show = scissors
    print(scissors)

if user_choice == comp_choice:
    print("It is a draw.")
elif ((user_choice == 1) and (comp_choice == 2)) or ((user_choice == 2) and (comp_choice == 3)) or ((user_choice == 3) and (comp_choice == 1)):
    print("Computer wins.")
elif ((user_choice == 1) and (comp_choice == 3)) or ((user_choice == 2) and (comp_choice == 1)) or ((user_choice == 3) and (comp_choice == 2)):
    print("You win.")
