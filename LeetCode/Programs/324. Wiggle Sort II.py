class Solution(object):
  def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # sort nums
    # find midpoint
    # set alt indices to 1st half and 2nd half
    nums.sort()
    mid = len(nums[::2])-1
    nums[::2],nums[1::2] = nums[mid::-1],nums[:mid:-1]