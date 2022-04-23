class Solution(object):
    def isValid(self, s):
        stack = []
        openBrace = '{(['
        oppDict = {'(':')','[':']','{':'}'}
        for sym in s:
            if sym in openBrace:
                stack.append(sym)
            elif len(stack) == 0:
                return False
            elif oppDict[stack.pop()] != sym:
                return False
        return True if len(stack)==0 else False

sl = Solution()
print(sl.isValid('()'))

a = ['(']
print(a.pop())