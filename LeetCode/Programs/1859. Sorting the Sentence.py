class Solution:
    def sortSentence(self, s: str) -> str:
        broken = s.split(' ')
        numWords = len(broken)
        if numWords < 2:
            return s[:-1]
        wordList = [''] * numWords
        for word in broken:
            wordList[int(word[-1])-1] = word[:-1]
        resSent = ''
        for word in wordList:
            resSent += word + ' '
        return resSent[:-1]