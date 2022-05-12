import imp


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        lenS = len(s)
        if lenS < k:
            return lenS
        maxSeqLen = i = 0
        while i < (lenS-1) and i < (lenS - maxSeqLen - 1) :
            j = i + 1
            currSeqLen = 1
            numReplace = 0
            while numReplace <= k and j < lenS:
                currSeqLen += 1
                if s[j] != s[i]:
                    numReplace += 1
                j += 1
            # currSeqLen -= int(numReplace > k)
            maxSeqLen = max(maxSeqLen, currSeqLen)
            if j == lenS:
                return maxSeqLen
            i += 1
            while i < (lenS-1) and s[i] == s[i+1]:
                i += 1
        return maxSeqLen

s = Solution()
print(s.characterReplacement("AABABBA", 1))