# from collections import defaultdict

# class Solution(object):
#     def characterReplacement(self, s, k):
#         """
#         :type s: str
#         :type k: int
#         :rtype: int
#         """
#         lenS = len(s)
#         if lenS < k:
#             return lenS
#         # print(lenS, 'l')
#         letterCounts = defaultdict(int)
#         for c in s:
#             letterCounts[c] += 1
#         maxRepeatingLetterCount = 0
#         def refreshMaxRepeatingLetter():
#             maxCount = 0
#             maxChar = ''
#             for c in letterCounts:
#                 if letterCounts[c] > maxCount:
#                     maxCount = letterCounts[c]
#                     maxChar = c
#             return maxChar, maxCount
#         maxRepeatingLetter, maxRepeatingLetterCount = refreshMaxRepeatingLetter()
#         while (lenS-maxRepeatingLetterCount) > k:
#             print(lenS, maxRepeatingLetterCount, lenS-maxRepeatingLetterCount, k, s)
#             if letterCounts[s[0]] > letterCounts[s[-1]]:
#                 letterCounts[s[-1]] -= 1
#                 if s[-1] == maxRepeatingLetter:
#                     maxRepeatingLetter, maxRepeatingLetterCount = refreshMaxRepeatingLetter()
#                 s = s[:-1]
#             elif letterCounts[s[0]] < letterCounts[s[-1]]:
#                 letterCounts[s[0]] -= 1
#                 if s[0] == maxRepeatingLetter:
#                     maxRepeatingLetter, maxRepeatingLetterCount = refreshMaxRepeatingLetter()
#                 s = s[1:]
#             else:
#                 lCount,rCount = 1,1
#                 while s[-(rCount + 1)] == s[-1]:
#                     rCount += 1
#                 while s[lCount] == s[0]:
#                     lCount += 1
#                 if rCount > lCount:
#                     letterCounts[s[0]] -= 1
#                     if s[0] == maxRepeatingLetter:
#                         maxRepeatingLetter, maxRepeatingLetterCount = refreshMaxRepeatingLetter()
#                     s = s[1:]
#                 else:
#                     letterCounts[s[-1]] -= 1
#                     if s[-1] == maxRepeatingLetter:
#                         maxRepeatingLetter, maxRepeatingLetterCount = refreshMaxRepeatingLetter()
#                     s = s[:-1]
#             lenS -= 1
#         print(s)
#         return lenS

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = {}
        l = 0
        maxF = 0
        res = 0
        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            maxF = [maxF, counts[s[r]]][maxF < counts[s[r]]]

            while (r-l+1) - maxF > k:
                counts[s[l]] -= 1
                l += 1
            
            res = [res, r-l+1][res < r-l+1]
        return res

s = Solution()
# print(s.characterReplacement("KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF", 4))
print(s.characterReplacement("ABA", 0))
