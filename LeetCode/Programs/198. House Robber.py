class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:   return max(nums)
        w1,wo1,w2,wo2 = nums[0],0,nums[1],nums[0]
        for n in nums[2:]:
            w1,wo1 = max(w1,wo1,wo2)+n,max(w1,wo1,w2,wo2)
            w1,wo1,w2,wo2 = w2,wo2,w1,wo1
        
        return max(w2,wo2)