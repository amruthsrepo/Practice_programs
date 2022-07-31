class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        retList = [0] * len(temperatures)
        for i in range(len(temperatures)-2,-1,-1):
            # print(i,'a', retList)
            foundAt = i + 1
            skipped = 1
            while foundAt < len(temperatures):
                if temperatures[foundAt] > temperatures[i]:
                    retList[i] = skipped
                    break
                elif retList[foundAt] == 0:
                    retList[i] = 0
                    break
                skipped += retList[foundAt]
                foundAt += retList[foundAt]
        return retList