class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numCounts = [0] * len(nums)
        for n in nums:
            if numCounts[n] > 0:
                return n
            numCounts[n] += 1