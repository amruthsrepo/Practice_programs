class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        t = ''
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~ `'''
        for i in range(len(s)):
            if s[i] not in punc:
                t += s[i]
        end,start = len(t)-1,0
        while start<end:
            if t[start] != t[end]:
                return False
            start += 1
            end -= 1
        return True

sl = Solution()
print(sl.isPalindrome("A man, a plan, a canal: Panama"))