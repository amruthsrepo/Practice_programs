class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retList = [[]]
        for i in range(1, len(nums)+1):
            retList.extend(self.subsetUtil(list(nums), i, []))
        return retList
        
    def subsetUtil(self, nums, size, preList):
        retList = []
        if len(preList) == size-1:
            while (len(nums) + len(preList)) >= size:
                preList.append(nums.pop())
                retList.append(list(preList))
                preList.pop()
            return retList
        while (len(nums) + len(preList)) >= size:
            preList.append(nums.pop())
            retList.extend(self.subsetUtil(list(nums), size, preList))
            preList.pop()
        return retList