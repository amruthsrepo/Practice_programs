class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        lString, rString = 0, 0
        lMap, rMap = {}, {}
        numGoodStrings = 0
        for c in s:
            if rMap.get(c, 0) > 0:
                rMap[c] += 1
            else:
                rMap[c] = 1
                rString += 1
            lMap[c] = 0
        for c in s:
            rMap[c] -= 1
            rString -= int(not rMap[c])
            lString += int(not lMap[c])
            lMap[c] += 1
            numGoodStrings += int(lString == rString)
        return numGoodStrings

s = Solution()
print(s.numSplits("aacaba"))
print(s.numSplits("abcd"))