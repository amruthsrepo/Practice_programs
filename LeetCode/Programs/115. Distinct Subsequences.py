# method 1 =>
import copy
class Solution1(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # for each char in s: find count of all letters ahead
        # for each char in t: add number of ways that and leading letter found into a list

        if len(s) < len(t): return 0
        nextIndList = []
        sLetterCounts,currentCounts = {},{}
        print('a')
        for i in range(len(s)-1,-1,-1):
            c = s[i]
            sLetterCounts[(i,c)] = copy.deepcopy(currentCounts)
            currentCounts[c] = currentCounts.get(c, [])
            currentCounts[c].append(i)
            # print(c, currentCounts[c])
            if c == t[0]:   nextIndList.append(i)
        print('b', s,t)
        totalWays = 0
        nextIndList1 = []
        for i in range(len(t)-1):
            c,cNext = t[i],t[i+1]
            for j in nextIndList:
                # if (j,c) in sLetterCounts and cNext in sLetterCounts[(j,c)]:
                nextIndices = sLetterCounts.get((j,c), {}).get(cNext, [])
                nextIndList1.extend(nextIndices)
                # print(c,j,nextIndices)
            nextIndList,nextIndList1 = nextIndList1,[]
        
        for i in nextIndList:
            totalWays += ((i,t[-1]) in sLetterCounts)
        
        return totalWays

# method 2 ==>
class Solution2(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        numWays = {}

        def dfs(i,j):
            if j == len(t): return 1
            if i == len(s): return 0
            if (i,j) in numWays:    return numWays[(i,j)]

            numWays[(i,j)] = dfs(i+1,j)
            if s[i] == t[j]:    numWays[(i,j)] += dfs(i+1, j+1)

            return numWays[(i,j)]
        
        return dfs(0,0)