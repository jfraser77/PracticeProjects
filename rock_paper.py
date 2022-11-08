"""
Name: Joe Fraser
Date: 10/17/22
Description: Rock paper scissors project
"""

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

def main():

    rps = [rock, paper, scissors]

    computer_choice = random.randint(0, 2)

    gamer_choice = int(input("Choose rock(), paper, or scissors shoot! "))

    if gamer_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice > gamer_choice:
        print("You lose")
    elif computer_choice == gamer_choice:
        print("It's a draw")
    else: 
        print("Invalid entry")





if __name__ == "__main__":
    main()