from typing import List
from collections import Counter


class Solution:

    def __init__(self):
        self.factorialVals = {}

    def isPowerOfTwo(self, num: int) -> int:
        return True if (num & num - 1) == 0 else False

    def factorial(self, num: int) -> int:
        if num in self.factorialVals:
            return self.factorialVals[num]
        else:
            res = 1
            for i in range(2, num + 1):
                res *= i
            self.factorialVals[num] = res
            return res

    def nCr(self, n: int, r: int) -> int:
        return int(self.factorial(n) / (self.factorial(r) * self.factorial(n-r)))

    def countPairs(self, deliciousness: List[int]) -> int:
        if len(deliciousness) == 1:
            return 0
        else:
            countDict = Counter(deliciousness)
            numPairs = 0
            deliciousness = list(countDict.keys())
            numUnique = len(deliciousness)
            addedToSum = []
            if self.isPowerOfTwo(deliciousness[numUnique - 1] * 2) and countDict[deliciousness[numUnique - 1]] > 1:
                numPairs += self.nCr(
                    countDict[deliciousness[numUnique - 1]], 2)
                addedToSum.append(
                    (deliciousness[numUnique - 1], deliciousness[numUnique - 1]))
            for i in range(numUnique - 1):
                if self.isPowerOfTwo(deliciousness[i] * 2) and countDict[deliciousness[i]] > 1:
                    numPairs += self.nCr(countDict[deliciousness[i]], 2)
                    addedToSum.append((deliciousness[i], deliciousness[i]))
                for j in range(i + 1, numUnique):
                    if self.isPowerOfTwo(deliciousness[i] + deliciousness[j]):
                        numPairs += countDict[deliciousness[i]
                                              ] * countDict[deliciousness[j]]
                        addedToSum.append((deliciousness[i], deliciousness[j]))

            return numPairs


s = Solution()
print(s.countPairs([2160, 1936, 3, 29, 27, 5, 2503, 1593, 2, 0, 16, 0, 3860, 28908, 6, 2, 15, 49,
      6246, 1946, 23, 105, 7996, 196, 0, 2, 55, 457, 5, 3, 924, 7268, 16, 48, 4, 0, 12, 116, 2628, 1468]))
print(s.countPairs([0, 0, 0, 0]))
print(s.countPairs([1, 3, 5, 7, 9]))
print(s.countPairs([1, 1, 1, 3, 3, 3, 7]))
