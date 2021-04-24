from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputArray, indexDict, numAna = [], {}, 0
        for word in strs:
            strSorted = "".join(sorted(word))
            if strSorted in indexDict:
                outputArray[indexDict[strSorted]].append(word)
            else:
                indexDict[strSorted] = numAna
                outputArray.append([])
                outputArray[numAna].append(word)
                numAna += 1
        return outputArray


s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))
