class Solution(object):
    def hammingWeight(self, n):
        num1s = 0
        while n:
            n = n & (n-1)
            num1s += 1
        return num1s