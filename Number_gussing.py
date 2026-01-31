import numpy as np
import sys

# Getting input from user for range
try:
    a = int(input("Enter the lower limit of range:"))
except ValueError:
    sys.exit("Please Enter a valid input")
try:
    b = int(input("Enter the upper limit of range:"))
except ValueError:
    sys.exit("Please Enter a valid input")
if (a >= b ):
    sys.exit("Please enter a valid input")

# Generating random number
random = np.random.randint(a,b)
#for program testing purpose
print(random)

#actual code for number guessing
guess = None
while (guess != random ):
    try:
        guess = int(input(f"Guess a number from {a} to {b} :"))
    except ValueError:
         continue
    if (guess > b or guess <a):
        print("Enter a valid input")
        continue
    elif (guess == random ):
            print("Your guess was correct")
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
