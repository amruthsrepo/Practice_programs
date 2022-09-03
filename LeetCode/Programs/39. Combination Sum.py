class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        return self.combinationSumUtil(candidates, target, [])
        
    def combinationSumUtil(self, candidates, target, preList):
        retList = []
        for i in range(len(candidates)):
            if candidates[i] > target:
                return retList
            preList.append(candidates[i])
            if candidates[i] == target:
                retList.append(list(preList))
                return retList
            retList.extend(self.combinationSumUtil(candidates[i:], (target-candidates[i]), list(preList)))
            preList.pop()
        return retList