class Solution(object):
    def maxSubArray(self, nums):
        lenArr = len(nums)
        currSubarr = nums[0]
        maxSubarr = nums[0]
        for r in range(1, lenArr):
            if currSubarr < 0:
                currSubarr = 0
            currSubarr += nums[r]
            maxSubarr = max(maxSubarr, currSubarr)
        return maxSubarr

sl = Solution()
print(sl.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(sl.maxSubArray([1]))
print(sl.maxSubArray([-1]))
print(sl.maxSubArray([5,4,-1,7,8]))
print(sl.maxSubArray([-2,1]))
print(sl.maxSubArray([-2,-1]))
print(sl.maxSubArray([-1,-2]))