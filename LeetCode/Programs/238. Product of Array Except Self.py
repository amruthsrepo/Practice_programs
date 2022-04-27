class Solution(object):
    def productExceptSelf(self, nums):
        allProduct = 1
        numZeros = 0
        for n in nums:
            if n != 0:
                allProduct *= n
                continue
            numZeros += 1
        if numZeros > 1:
            return [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = allProduct
                continue
            nums[i] = 0 if numZeros else allProduct / nums[i]
        return nums