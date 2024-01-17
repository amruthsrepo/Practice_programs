# In this problem, the goal is to determine the maximum value of an element at a certain index in an array of integers that can be constructed under some constraints.
# More specifically, n is the desired array size, maxSum is the maximum allowed sum of elements in the array, and kis the index of the element that needs its value to be maximized. The 0-indexed array has the following constraints:
# 1. The array consists of n positive integers.
# 2. The sum of all elements in the array is at most maxsum.
# 3. The absolute difference between any two consecutive elements in the array is at most 1.
# What is the maximum value of the integer at index k in such an array?
# For example, let's say n = 3, maxSum = 6, and k = 1. So, the goal is to find the maximum value of the element at index 1 in an array of 3 positive integers, where the sum of elements is at most 6, and the absolute difference between every two consecutive elements is at most 1.
# The maximum such value is 2, and it can be achieved, for example, by the array [1, 2, 2]. This array has 3 elements, each of them a positive integer. The sum of the elements does not exceed 6, and the absolute difference between any two consecutive elements is at most 1. There is no other such array that has a larger
# value at index k = 1. Therefore, the answer is 2 because that is the maximum value
# of the integer at index k.


def maxElement(n, maxSum, k):
    print(n, maxSum, k)
    if k > n:
        return -1
    if n == 1:
        return maxSum
    if n == maxSum:
        return 1

    remaining = maxSum - n
    numSteps = (remaining**0.5) // 1

    maxNum = 1 + numSteps
    remaining -= numSteps**2
    maxNum += remaining // n

    fromEnds = min(k, n - k)
    numN = 0
    sumN = 0
    remaining = maxSum - n
    while sumN <= remaining:
        numN += 1
        sumN += numN
    numFromEnds = numN - fromEnds

    print(maxNum, numFromEnds)
    return int(max(maxNum, numFromEnds))
