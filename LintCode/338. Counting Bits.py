class Solution(object):
    def countBits(self, n):
        retList = [0] * (n+1)
        i = j = 1
        while i <= n:
            if i & (i-1) == 0:
                j = 1
                retList[i] = 1
                i += 1
                continue
            retList[i] = 1 + retList[j]
            i += 1
            j += 1
        return retList