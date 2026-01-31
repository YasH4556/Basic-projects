import numpy as np
import sys

# Getting input from user for range
a = input("Enter the lower limit of range:")
if (a ==""):
    a = 1
else:
    a = int(a)
b = input("Enter the upper limit of range:")
if (b==""):
    b = 100
else:
    b = int(b)
    if (a >= b ):
        sys.exit("Please enter a valid input")

# Generating random number
random = np.random.randint(a,b)
#for program testing purpose
print(random)

#actual code for number guessing
guess = None
while (guess != random ):
    guess = input(f"Guess a number from {a} to {b} :")
    if (guess == "" or b <= int(guess) <= a):
        print("Please enter a valid guess")
    else:
        guess = int(guess)
        if (guess == random ):
            print("Your guess was correct")
            break
        else :
            percent = (abs(guess - random) - 1)/(b-a+1)
            if (percent <= 0.1):
                print("Soo close! You were almost their")
            elif(percent <=0.5):
                print("Close! You can do better")
            elif (percent <= 0.75):
                print("Not close! Try again")
            else:
                print("Way off! You need to improve a lot")
