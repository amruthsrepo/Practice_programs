class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 2:
            return ['()']
        n *= 2
        def util(sum = 1, parenthesisStr = '('):
            if len(parenthesisStr) == n:
                retList.append(parenthesisStr)
            else:
                if sum < n - len(parenthesisStr):
                    util(sum+1, parenthesisStr + '(')
                if sum > 0:
                    util(sum-1, parenthesisStr+')')

        retList = []
        util()
        return retList


s = Solution()
print(s.generateParenthesis(3))