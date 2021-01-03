class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            s = s.strip()
            float(s)
            return True if s != 'e' else False
        except:
            return False


s = Solution()
s.isNumber('01')
