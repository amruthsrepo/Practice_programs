class Solution(object):
    def isAnagram(self, s, t):
        l = len(s)
        if l != len(t):
            return False
        dictS = defaultdict(int)
        dictT = defaultdict(int)
        hashSet = set()
        for i in range(l):
            dictS[s[i]] += 1
            dictT[t[i]] += 1
            hashSet.add(s[i])
            hashSet.add(t[i])
        for a in hashSet:
            if dictS[a] != dictT[a]:
                return False
        return True