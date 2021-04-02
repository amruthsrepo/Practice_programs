from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        rainLen = len(rains)
        returnArray = [-1] * rainLen
        if rainLen < 2:
            return returnArray
        else:
            filled, canEmpty = {}, []
            for i in range(rainLen):
                if rains[i] == 0:
                    returnArray[i] = 1
                    if len(filled) == 0:
                        canEmpty = []
                    else:
                        canEmpty.append(i)
                elif rains[i] not in filled:
                    filled[rains[i]] = i
                elif len(canEmpty) > 0:
                    for j in canEmpty:
                        if j < filled[rains[i]]:
                            continue
                        else:
                            break
                    if j < filled[rains[i]]:
                        return []
                    returnArray[j] = rains[i]
                    canEmpty.remove(j)
                    filled[rains[i]] = i
                else:
                    return []
            return returnArray


s = Solution()
print([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2],
      s.avoidFlood([2, 3, 0, 0, 3, 1, 0, 1, 0, 2, 2]))
print([1, 0, 2, 0, 2, 1], s.avoidFlood([1, 0, 2, 0, 2, 1]))
print([1, 2, 0, 0, 2, 1, 1], s.avoidFlood([1, 2, 0, 0, 2, 1, 1]))
print([1, 0, 0, 1, 1], s.avoidFlood([1, 0, 0, 1, 1]))
print([0, 1, 1], s.avoidFlood([0, 1, 1]))
print([1, 2, 0, 0, 2, 1], s.avoidFlood([1, 2, 0, 0, 2, 1]))
print([1, 2, 0, 1, 2], s.avoidFlood([1, 2, 0, 1, 2]))
print([1, 2, 0, 1], s.avoidFlood([1, 2, 0, 1]))
print([69, 0, 0, 0, 69], s.avoidFlood([69, 0, 0, 0, 69]))
