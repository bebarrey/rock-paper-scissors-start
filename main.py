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
print("Welcome to rock, paper, scissors.")
answer = input("Type '0' for rock, '1' for paper and '2' for scissors.\n")

print(f"You Chose: {answer}")
if answer == "0":
  print(rock)
elif answer == "1":
  print(paper)
elif answer == "2":
  print(scissors)



computer = random.randint(0,2)

print(f"Computer chose: {computer}")

if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
elif computer == 2:
  print(scissors)

if computer == 0 and answer == "2":
  print("Computer Wins.")
elif answer == "0" and computer == 2:
  print("You win.")
elif computer == 0 and answer == "0":
  print("Its a draw.") 

if computer == 2 and answer == "1":
  print("Computer Wins.")
elif answer == "2" and computer == 1:
  print("You win.")
elif computer == 2 and answer == "2":
  print("Its a draw.") 

if computer == 1 and answer == "0":
  print("Computer Wins.")
elif answer == "1" and computer == 0:
  print("You win.")
elif computer == 1 and answer == "1":
  print("Its a draw.")   