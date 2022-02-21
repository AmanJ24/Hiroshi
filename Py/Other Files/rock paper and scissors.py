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
import random 
choices = [rock, paper, scissors]
computer_chose = random.randint(0,2)
chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if(chose == 0 or chose == 1 or chose == 2):

    print(f"You chose:\n{choices[chose]} \n\n The computer chose:\n{choices[computer_chose]}")

    if(chose == 0 and computer_chose == 0):
        print("It's a draw.")
    elif(chose == 0 and computer_chose == 1):
        print("paper beats Rock. So, Computer won.")
    elif(chose == 0 and computer_chose == 2):
        print("Rock beats scissors. So, You won!")
    elif(chose == 1 and computer_chose == 0):
        print("Paper beats Rock. So, You won!")
    elif(chose == 1 and computer_chose == 1):
        print("It's a draw.")
    elif(chose == 1 and computer_chose == 2):
        print("Scissors beats Paper. So, Computer won.")
    elif(chose == 2 and computer_chose == 0):
        print("Rock beats Scissors. So, Computer won")
    elif(chose == 2 and computer_chose == 1):
        print("Scissors beats Paper. So, You won!")
    elif(chose == 2 and computer_chose == 2):
        print("It's a draw.")            

else:
    print("You entered an invalid number.")
