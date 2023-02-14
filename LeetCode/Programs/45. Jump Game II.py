from heapq import heappush
class Solution(object):
  def jump(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    numJumps = [list() for _ in range(len(nums))]
    # print(numJumps)
    heappush(numJumps[0], 0)
    i = 0
    for n in nums:
        minJumps = numJumps[i][0] + 1
        # print(i,n,minJumps, numJumps[i])
        i += 1
        for j in range(i, min(i+n, len(nums))):
            heappush(numJumps[j], minJumps)
    # print(numJumps)
    return numJumps[-1][0]