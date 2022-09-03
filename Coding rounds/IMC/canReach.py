#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'canReach' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER c
#  2. INTEGER x1
#  3. INTEGER y1
#  4. INTEGER x2
#  5. INTEGER y2
#

def canReach(c, x1, y1, x2, y2):
    while x2 >= x1 and y2 >= y1:
        x2Copy, y2Copy = x2, y2
        if x2 > y2:
            if y2 > y1:
                x2 %= y2
            else:
                return 'Yes' if ((x2 - x1) % y2 == 0) else 'No'
        elif y2 > x2:
            if x2 > x1:
                y2 %= x2
            else:
                return 'Yes' if ((y2 - y1) % x2 == 0) else 'No'
        x2 %= c
        y2 %= c
        x2Copy2, y2Copy2 = x2, y2
        if x2 == x1 and y2 == y1:
            return 'Yes'
        else:
            x2, y2 = x2Copy2, y2Copy2
    
    return 'Yes' if (x2 == x1 and y2 == y1) else 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    result = canReach(c, x1, y1, x2, y2)

    fptr.write(result + '\n')

    fptr.close()
