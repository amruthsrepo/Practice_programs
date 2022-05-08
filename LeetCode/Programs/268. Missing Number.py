class Solution(object):
    def missingNumber(self, nums):
        for i in range(1,len(nums)):
            nums[0] += nums[i]
        return ((len(nums) * (len(nums) + 1)) / 2) - nums[0]