
# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept 16, 2026
# Purpose: Practice using if, elif, and else statments.
# Usage: ./lab2c.py

# TO DO 1:
# Prmopt the user to enter a sentence, save it in the variable str1
# Prmopt the user to enter another sentence, save it in the variable str2
#
# Use if, elif, and else statments with the len() function to check which of the 2 is longer.
# The final result should be:
# ---- is longer then ----
# If they are equal then print:
# ---- and ---- are equal.
# Get input from the user
str1 = (input("Write out a sentence."))
str2 = (input("How about a second sentence?"))

x = len(str1)
y = len(str2)

if (x > y):
    print(str1, "is greater than", str2)
elif (y >x):
    print(str2, "is greater than", str1)
elif (x == y):
    print(str1, "and", str2, "are equal.")