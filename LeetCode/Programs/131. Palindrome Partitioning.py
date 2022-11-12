class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.partUtil(s, 0, [], [])

    def partUtil(self, s, start, curList, retList):
        if start == len(s):
            retList.append(curList)
            return retList
        prevList = list(curList)
        end = start + 1
        while end <= len(s):
            sTemp = s[start:end]
            if sTemp == sTemp[::-1]:
                curList = list(prevList)
                curList.append(s[start:end])
                self.partUtil(s, end, curList, retList)
            end += 1
        return retList