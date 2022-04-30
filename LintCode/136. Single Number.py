# Q. Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        r = 0
        for n in nums:
            # Performs bitwise XOR operation so whatever appeares 2 times is cancelled
            r = r ^ n
        return r