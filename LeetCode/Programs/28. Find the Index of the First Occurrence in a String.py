class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        letters = {}
        nSize = len(needle)
        for i in range(nSize):
            n,h = needle[i], haystack[i]
            letters[n] = letters.get(n, 0) + 1
            if not letters[n]: del letters[n]
            letters[h] = letters.get(h, 0) - 1
            if not letters[h]: del letters[h]
        i += 1
        if not letters and haystack[i-nSize:i] == needle:
            return i - nSize
        while i < len(haystack):
            n,h = haystack[i-nSize], haystack[i]
            letters[n] = letters.get(n, 0) + 1
            if not letters[n]: del letters[n]
            letters[h] = letters.get(h, 0) - 1
            if not letters[h]: del letters[h]
            i += 1
            # print(letters, haystack[i-nSize:i], needle)
            if not letters and haystack[i-nSize:i] == needle:
                return i - nSize
        return -1