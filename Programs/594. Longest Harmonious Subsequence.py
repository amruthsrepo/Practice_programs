from typing import List
from collections import Counter


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        maxArrLen = 0
        countDict = Counter(nums)
        for key in countDict:
            if key-1 in countDict:
                maxArrLen = max(maxArrLen, countDict[key] + countDict[key - 1])
            if key+1 in countDict:
                maxArrLen = max(maxArrLen, countDict[key] + countDict[key + 1])
        return maxArrLen


s = Solution()
print(s.findLHS([1, 3, 2, 2, 5, 2, 3]))
print(s.findLHS([1, 1, 1, 1]))
print(s.findLHS([1]))
print(s.findLHS([1, 0]))
print(s.findLHS([0, 1, 0]))
