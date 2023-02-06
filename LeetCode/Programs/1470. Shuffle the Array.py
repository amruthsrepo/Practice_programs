class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        numsy, nums = nums[n:], nums[:n]
        retNums = []
        while nums:
            retNums.append(nums.pop(0))
            retNums.append(numsy.pop(0))
        return retNums