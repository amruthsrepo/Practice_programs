#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMostVisited' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY sprints
#

def getMostVisited(n, sprints):
    numCounts = [0] * (n+2)
    for i in range(len(sprints)-1):
        s,e = min(sprints[i], sprints[i+1]), max(sprints[i], sprints[i+1])
        numCounts[s] += 1
        numCounts[e+1] -= 1
    maxC, maxI = -1, -1
    # print(numCounts)
    hitRate = 0
    # hitRateArr = [0] * (n+1)
    for i in range(1, n+1):
        hitRate += numCounts[i]
        # hitRateArr[i] = hitRate
        # print(i, hitRate, numCounts[i])
        if hitRate > maxC:
            maxC = hitRate
            maxI = i
    return maxI

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sprints_count = int(input().strip())

    sprints = []

    for _ in range(sprints_count):
        sprints_item = int(input().strip())
        sprints.append(sprints_item)

    result = getMostVisited(n, sprints)

    fptr.write(str(result) + '\n')

    fptr.close()
