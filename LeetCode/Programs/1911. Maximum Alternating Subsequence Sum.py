class Solution(object):
  def maxAlternatingSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    plusMax,minusMax = 0,0

    for n in nums:
      plusMax = max(plusMax,minusMax+n)
      minusMax = max(minusMax,plusMax-n)

    return max(plusMax,minusMax)