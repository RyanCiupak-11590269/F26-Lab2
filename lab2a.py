# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept 16, 2026
# Purpose: Create a variable, check its type and print the variable.
# Usage: ./lab2a.py


x = input("Choose a number")
print(type(x))
x = int(x)
print(type(x))
if (x >= 6) is True:
    print(x,"is greater than 6!")
if (x > 4) and (x < 12) is True:
    print(x, "is greater than 4 and less than 12!")