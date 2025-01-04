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
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for rock,"
               "1 for Paper, 2 for Scissors \n"))
if choice >=0 and  choice <=2:
    print(game_images[choice])
rand = random.randint(0,2)
print("Computer Chose:")
print(game_images[rand])

if choice >= 3 or choice < 0:
    print("Invalid number, you lose!")
elif choice ==0 and rand == 2:
    print("You win!")
elif rand == 0 and choice ==2:
     print("You win!")
elif rand > choice:
    print("You lose!")
elif choice > rand:
    print("You win!")
elif choice == rand:
    print("Its a draw!")