class Solution(object):
    def countNicePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumCounts = {}
        for i in range(len(nums)):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
            sumCounts[nums[i]] = sumCounts.get(nums[i], 0) + 1
        numGoodPairs = 0
        for k in sumCounts:
            if sumCounts[k] > 1:
                numGoodPairs += (sumCounts[k] * (sumCounts[k] - 1)) / 2
        return numGoodPairs % ((10**9) + 7)