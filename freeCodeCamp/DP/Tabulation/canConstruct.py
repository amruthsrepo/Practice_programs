class Solution:
    def canConstruct(self, target, words):
        boolArray = [False] * (len(target) + 1)
        boolArray[0] = True
        wordDict = {}
        for w in words:
            firstLetter = w[0]
            wordDict[firstLetter] = wordDict.get(firstLetter, [])
            wordDict[firstLetter].append(w)
        for i in range(len(target)):
            if boolArray[i] and target[i] in wordDict:
                requiredLetters = len(target) - i
                for w in wordDict[target[i]]:
                    if len(w) <= requiredLetters and target[i:i+len(w)] == w:
                        boolArray[i+len(w)] = True
        return boolArray[-1]

s = Solution()
print(s.canConstruct('abcdef', ['ab','abc','cd','def','abcd']))
print(s.canConstruct('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(s.canConstruct('skateboard', ['bo','rd','ate','t','ska','sk','boar']))