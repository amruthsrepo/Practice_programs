from heapq import heapify, heappop, heappush


class Solution(object):
    def lastStoneWeight(self, stones):
        stones = [-i for i in stones]
        numStones = len(stones)
        while numStones > 1 :
            heapify(stones)
            heappush(stones, heappop(stones) - heappop(stones))
            print(stones)
            numStones -= 1
        if numStones < 1: return 0
        return -stones[0]
