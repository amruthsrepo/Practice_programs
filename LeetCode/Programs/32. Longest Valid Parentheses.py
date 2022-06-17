class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for c in s:
            if c == '(':
                sum += 1
            else:
                sum -= 1
        def trimStr(s, sum):
            while s and s[0] == ')':
                s = s[1:]
                sum += 1
            while s and s[-1] == '(':
                s = s[:-1]
                sum -= 1
            # while s and s[0] == '(' and sum > 0:
            #     s = s[1:]
            #     sum -= 1
            # while s and s[-1] == ')' and sum < 0:
            #     s = s[:-1]
            #     sum += 1
            while s and sum and s[0] == '(' and s[-1] == ')':
                lSum,lLen,rSum,rLen = 0,0,0,0
                for c in s:
                    if c == '(':
                        lSum += 1
                    else:
                        lSum -= 1
                    lLen += 1
                    if not lSum:
                        break
                if lLen == len(s) and not sum:
                    return s,sum
                for c in range(len(s)-1, -1, -1):
                    if s[c] == '(':
                        rSum += 1
                    else:
                        rSum -= 1
                    rLen += 1
                    if not rSum:
                        break
                if rLen > lLen:
                    s = s[lLen:]
                else:
                    s = s[:-rLen]
            return s, sum
        s,sum = trimStr(s, sum)
        while s and (sum or s[0] != '(' or s[-1] != ')'):
            s,sum = trimStr(s, sum)
        return len(s)

s = Solution()
print(s.longestValidParentheses(")(())))(())())"))
print(s.longestValidParentheses("()(()"))
print(s.longestValidParentheses("(()"))