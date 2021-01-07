import re


class Solution:
    def myAtoi(self, s: str) -> int:
        t, s = 0, s.strip().split(' ')[0]
        if len(s) == 0:
            return 0
        try:
            t = int(re.findall("((^[\-\+\.]\d+)|(^(\-\.)\d+)|(^(\+\.)\d+)|(^\d+))+", s)[0][0])
        except:
            return 0
        t = (t, (2**31)-1)[t > (2**31)-1]
        t = (t, -2**31)[t < -2**31]
        return t


s = Solution()
print(s.myAtoi('42'))
print(s.myAtoi('+456+abc123'))
print(s.myAtoi('words and 987'))
print(s.myAtoi('+42-'))
print(s.myAtoi('..42-'))
print(s.myAtoi('     -42'))
print(s.myAtoi('-91283472332'))
print(s.myAtoi('--4193 with words'))
print(s.myAtoi('-4193 with words'))
print(s.myAtoi('-4193-4193 with words'))
