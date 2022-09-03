class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permuteUtil(nums, [])
        
    def permuteUtil(self, nums, preList = []):
        if len(nums) == 1:
            preList.append(nums.pop())
            return [preList]
        retList = []
        for i in range(len(nums)):
            preList.append(nums.pop(i))
            retList.extend(self.permuteUtil(list(nums), list(preList)))
            nums.insert(i, preList.pop())
        return retList