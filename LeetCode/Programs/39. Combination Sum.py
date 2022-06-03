class Solution(object):
    def combinationSum(self, candidates, target, mainCall = True):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not len(candidates): return []
        candidates = sorted(candidates)
        retList = []
        if target in candidates:
            retList.append([target])
            candidates.remove(target)
        while candidates[-1] >= target and mainCall:
            candidates.pop()
        targetList = []
        targetListSum = 0
        for n in candidates:
            targetListSum += n
            targetList.append(n)
            if targetListSum == target:
                retList.append(list(targetList))
            elif targetListSum > target and (mainCall or len(targetList) != len(candidates)):
                combi = self.combinationSum(targetList, targetListSum - target, False)
                for c in combi:
                    toAdd = list(set(targetList) - set(c))
                    if (not mainCall or len(c) > 1) and toAdd not in retList:
                        retList.append(toAdd)
        return retList

s = Solution()
for o in s.combinationSum([2,3,6,7], 7):
    print(o)
# for o in s.combinationSum([1,2,3,4,5,6,7,8,9], 15):
#     print(o)