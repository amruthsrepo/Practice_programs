class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) < 1:
            return []
        numDict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        retList = []
        def genCombi(genStr = ''):
            if len(genStr) == len(digits):
                retList.append(genStr)
            else:
                for l in numDict[digits[len(genStr)]]:
                    genCombi(genStr + l)
        genCombi()
        return retList

s = Solution()
print(s.letterCombinations("23"))