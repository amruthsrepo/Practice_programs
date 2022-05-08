class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)
        maxSeqLen = 0
        seqStartAt = 0
        lastFoundAt = {}
        for i in range(len(s)):
            if s[i] in lastFoundAt:
                seqStartAt = max((lastFoundAt[s[i]] + 1), seqStartAt)
                lastFoundAt[s[i]] = i
            lastFoundAt[s[i]] = i
            maxSeqLen = max(maxSeqLen, i-seqStartAt+1)
        return maxSeqLen