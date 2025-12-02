# 1. Local scope: Variables defined within a function are in the local scope of that function.


# 2. A variable created in the main body of the program is a global variable and in a global scope. That mean it can be used anywhere including inside functions. 



import random
import datetime


player1 = input("Enter name for Player 1: ")
player2 = input("Enter name for Player 2: ")

random.seed(datetime.datetime.now().timestamp())  # Initialize the random number generator
roll1 = random.randint(1, 6)
roll2 = random.randint(1, 6)

if roll1 > roll2:
    print(f"{player1} wins with a roll of {roll1} against {roll2}!")    
elif roll2 > roll1:
    print(f"{player2} wins with a roll of {roll2} against {roll1}!")
else:
    print(f"It's a tie! Both players rolled a {roll1}!")