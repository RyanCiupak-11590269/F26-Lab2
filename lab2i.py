# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: September 23, 2026
# Purpose: Learn how to use while loops for validating user input.
# Usage: ./lab2i.py

# TO DO 1: 
# Creat variable pin. The value of pin should be a 4 digit code inputted by the user.
# Add a while loop to create program that wont end until the user enters 1234.
# Follow the specific instructions given in the README.md file.
#guess = 5
#number = int(input("Guess what number less than 10 I am thinking off?"))
#while number != guess:  # loop condition 
#  print("incorrect guess, try again...")
# number = int(input("Guess what number less than 10 I am thinking off?")) # keep taking input from user until the user enters the correct guess.
#print("You got it right!") # this statement will be executed when loop has terminated which will only happen when the user enters the number 5.
# Define the correct PIN

pin = 1234
guess = int(input("Guess the 4 digit pin."))
while guess != pin:
    print("Incorrect... Try again!")
    guess = int(input("Guess the 4 digit pin."))
print("Correct pin! You may enter")