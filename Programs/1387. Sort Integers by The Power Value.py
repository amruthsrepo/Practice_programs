from typing import List


class Solution:

    def __init__(self):
        self.stepsNeeded = {}

    def calcSteps(self, num: int) -> int:
        intermediateNums = [num]
        numSteps = 0
        while num != 1:
            if num in self.stepsNeeded:
                numSteps += self.stepsNeeded[num]
                num = 1
            elif num % 2 == 0:
                num /= 2
                intermediateNums.append(num)
                numSteps += 1
            else:
                num = (3 * num) + 1
                intermediateNums.append(num)
                numSteps += 1
        for i in range(len(intermediateNums)):
            self.stepsNeeded[intermediateNums[i]] = numSteps - i
        return numSteps

    def getKth(self, lo: int, hi: int, k: int) -> int:
        stepsforInput = []
        for i in range(hi, lo-1, -1):
            stepsforInput.insert(0, self.calcSteps(i))
        sortedIndices = sorted(range(len(stepsforInput)),
                               key=lambda k: stepsforInput[k])
        return lo + sortedIndices[k - 1]


s = Solution()
print(s.getKth(1, 1, 1))
print(s.getKth(12, 15, 2))
print(s.getKth(7, 11, 4))
print(s.getKth(10, 20, 5))
print(s.getKth(1, 1000, 777))
