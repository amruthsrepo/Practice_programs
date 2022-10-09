class Solution:
    def howSum(self, target, digits):
        howDict = {0:[[]]}
        howNums = [0]
        while howNums:
            currNum = howNums.pop(0)
            currList = list(howDict[currNum][0])
            for d in digits:
                currSum = currNum + d
                currList.append(d)
                if currSum == target:
                    return currList
                elif currSum < target:
                    howDict[currSum] = howDict.get(currSum, [])
                    howDict[currSum].append(list(currList))
                    howNums.append(currSum)
                currList.pop()
        return []

s = Solution()
print(s.howSum(14, [5,3,4]))
print(s.howSum(7, [5,3,4]))