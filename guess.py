import random

from matplotlib.style import use

name = input("Please enter your name: ")
print("Welcome to the 'Guess the number game' " + name)

secretNum = random.randint(1, 20)

for guesses in range(1, 6): #start at 1 instead of 0
    print("Guess the number between 1-20")
    userNum = int(input())
    if userNum < secretNum:
        print("Too low")
    elif userNum > secretNum:
        print("Too high")
    else:
        break 

if userNum == secretNum:
    print("You won!!")
else:
    print("Sorry you lost, the number was " + str(secretNum))

