# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Ryan Ciupak
# Date: September 23, 2026
# Purpose: use for loop.
# Usage: ./lab2k.py


total = 0
i = 0
for i in range(101):
    if i % 2 == 0:
        total = total + i
print(total)
