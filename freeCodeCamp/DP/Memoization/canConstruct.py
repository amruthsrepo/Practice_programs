class canConstruct:
    def solution(self, target, wordBank):
        wordDict = {}
        for w in wordBank:
            wordDict[w[0]] = wordDict.get(w[0], [])
            wordDict[w[0]].append(w)
        return self.solUtil(target, wordDict, 0)

    def solUtil(self, target, wordDict, startAt):
        if startAt >= len(target):
            return True
        if target[startAt] not in wordDict:
            return False
        numRemaining = len(target) - startAt
        for w in wordDict[target[startAt]]:
            if len(w) <= numRemaining and w == target[startAt:len(w)+startAt] and self.solUtil(target, wordDict, startAt+len(w)):
                return True
        return False


c = canConstruct()
print(c.solution('abcdef', ['ab','abc','cd','def','abcd']))
print(c.solution('enterapotentpot', ['a','p','ent','enter','ot','o','t']))
print(c.solution('skateboard', ['bo','rd','ate','t','ska','sk','boar']))