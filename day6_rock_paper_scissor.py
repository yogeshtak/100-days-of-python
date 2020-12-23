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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_ask = int(input("Select your option? 1 for Rock, 2 for Paper and 3 for Scissor"))

computer_opt = random.randint(1,3)

if computer_opt == user_ask:
    print("Game Tied")

if computer_opt == 1 and user_ask == 2:
    print("You won, computer selected Rock")
    print(rock)

if computer_opt == 1 and user_ask == 3:
    print("You lose, computer selected Rock")
    print(rock)

if computer_opt == 2 and user_ask == 1:
    print("You lose, Computer selected Paper")
    print(paper)

if computer_opt == 2 and user_ask == 3:
    print("You won, computer selected Paper")
    print(paper)

if computer_opt == 3 and user_ask == 1:
    print("You won, computer selected Scissor")
    print(scissor)  

if computer_opt == 3 and user_ask == 2:
    print("You lose, computer selected Scissor")
    print(scissor)