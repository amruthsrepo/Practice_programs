class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenNums = len(nums)
        if lenNums < 3:
            return []
        nums = sorted(nums)
        retList = []
        i = 0
        while i < (lenNums - 2):
            j = i + 1
            k = lenNums - 1
            while j < k:
                sumNum = nums[i] + nums[j] + nums[k]
                if sumNum == 0:
                    retList.append([nums[i], nums[j], nums[k]])
                elif sumNum > 0:
                    k -= 1
                    continue
                elif sumNum < 0:
                    j += 1
                    continue
                while nums[k] == nums[k-1] and k > (j + 1):
                    k -= 1
                k -= 1
                while nums[j] == nums[j+1] and j < (k - 1):
                    j += 1
                j += 1
            i += 1
            while nums[i] == nums[i-1] and i < lenNums - 2:
                i += 1
        return retList