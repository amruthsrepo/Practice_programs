#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumCost' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY red
#  2. INTEGER_ARRAY blue
#  3. INTEGER blueCost
#

def minimumCost(red, blue, blueCost):
    redLine, blueLine, lowestCost = [0] * (len(red)+1), [0] * (len(red)+1), [0] * (len(red)+1)
    blueLine[0] = blueCost
    for i in range(1, len(lowestCost)):
        redLine[i] = min(redLine[i-1] + red[i-1], blueLine[i-1] + red[i-1])
        blueLine[i] = min(blueLine[i-1] + blue[i-1], redLine[i-1] + blue[i-1] + blueCost)
        lowestCost[i] = min(redLine[i], blueLine[i])
    return lowestCost
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    red_count = int(input().strip())

    red = []

    for _ in range(red_count):
        red_item = int(input().strip())
        red.append(red_item)

    blue_count = int(input().strip())

    blue = []

    for _ in range(blue_count):
        blue_item = int(input().strip())
        blue.append(blue_item)

    blueCost = int(input().strip())

    result = minimumCost(red, blue, blueCost)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
