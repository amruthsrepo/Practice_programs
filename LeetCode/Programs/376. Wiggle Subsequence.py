class Solution(object):
  def wiggleMaxLength(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    lenNums,i = len(nums),1
    while i<len(nums) and nums[i] == nums[i-1]: i+=1
    if i == lenNums:  return 1
    isUp,maxSeq,i = nums[i-1]<nums[i],2,i+1
    while i<lenNums:
      if (isUp and nums[i-1]>nums[i]) or ((not isUp) and nums[i-1]<nums[i]):
        isUp = not isUp
        maxSeq += 1
      i += 1
    
    return maxSeq