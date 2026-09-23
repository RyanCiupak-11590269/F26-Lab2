# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: September 21, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2f.py

# TO DO 1: Follow the instructions given in README.md file
import sys
x = len(sys.argv) - 1
if (x >= 2):
    name = str(sys.argv[1])
    age = str(sys.argv[2])
    print("Hello {}, you are {}, and you provided".format(name, age), x, "arguments.")
elif (x == 0):
    print("This script requires at least two arguments. No arguments were provided!")
else:
    print("This script requires at least two arguments. You provided", x, "arguments.")