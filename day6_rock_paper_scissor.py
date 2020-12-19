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

user_ask = int(input("Select your option? 1 for Rock, 2 for Paper and 3 for Scissor"))

computer_opt = random.randint(0,2)

if computer_opt == user_ask:
    