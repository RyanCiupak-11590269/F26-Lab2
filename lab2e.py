# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: Sept 16, 2026
# Purpose: Learn how to use command line arguments.
# Usage: ./lab2e.py

# TO DO 1: Follow the instructions given in README.md file
import sys
x = len(sys.argv) - 1
if (x == 2):
    print("Hello user, good job, you provided two arguments")
elif (x == 0):
    print("This script requires exactly two arguments. No arguments were provided!")
else:
    print("This script requires exactly two arguments. You provided", x, "arguments.")