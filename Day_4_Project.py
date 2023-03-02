#RULES : 1. Rock wins over Scissors.
#        2. Scissors win against Paper.
#        3. Paper wins against Rock.
#The images i used here are taken from ASCII chart
import random
rock = ''' 
       \                       ___--._
       //-------------------./   ._. \)
                            |   / (_\_\)
                            |_ '  (___)
\                           |     (__)
 \__________________________|`------' 
 '''
paper = '''
                   _
               _  / |
              / \ | | /\
               \ \| |/ /
                \ Y | /___
              .-.) '. `__/
             (.-.   / /
                 | ' |
                 |___|
                [_____]
                |     |
'''
scissors = '''
    .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''
images = [rock, paper, scissors]

your_choice = int(input("Enter a number. 0 for ROCK, 1 for PAPER, 2 for SCISSORS ->->-> "))
print("You choose :")
if your_choice>=3 or your_choice<0:
    print("Your number is invalid, You lost")
else:
    print(images[your_choice])

    computer_choice = random.randint(0,2)
    print(f"\ncomputer chooses {computer_choice}")
    print(images[computer_choice])

    if your_choice>=3 or your_choice<0:
        print("Your number is invalid, You lost")
    elif your_choice==0 and computer_choice==2:
        print("Yay! You won the game")
    elif your_choice==0 and computer_choice==2:
        print("You lost the game!")
    elif computer_choice>your_choice:
        print("You lost the game!")
    elif your_choice>computer_choice:
        print("Yay! You won the game")
    elif your_choice==computer_choice:
        print("It's a draw game")
    print("\n")