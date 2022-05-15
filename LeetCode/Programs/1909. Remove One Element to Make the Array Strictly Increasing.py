class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return True
        isNotValid = False
        lenNums = len(nums)
        i = 1
        while i < lenNums:
            print(nums, nums[i], i, lenNums, nums[i] <= nums[i-1])
            if nums[i] <= nums[i-1]:
                if isNotValid:
                    return False
                isNotValid = True
                if i > 1:
                    prevNum = nums[i-2]
                else:
                    prevNum = float('-inf')
                if i < (lenNums - 1):
                    nextNum = nums[i+1]
                else:
                    nextNum = float('inf')
                if prevNum < nums[i] < nextNum:
                    nums.pop(i-1)
                    lenNums -= 1
                elif prevNum < nums[i-1] < nextNum:
                    nums.pop(i)
                    lenNums -= 1
                else:
                    return False
                i -= 2
            i = i + 1 + int(i == -1)
        return True

# true    [1,2,10,5,7]
# false   [1,1,1]
# true    [1,2,1]
# false   [2,3,1,2]
# true    [100,21,100]
# true    [100,101,21,102]
# false   [100,101,21,101]
# false   [1,4,1,2,3]