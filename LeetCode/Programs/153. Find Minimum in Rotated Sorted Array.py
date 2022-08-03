class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,len(nums)-1
        p = (-1 * ((-(r-l)) // 2)) + l
        lowest = r
        while r >= l:
            # print(l,p,r)
            if nums[p] > nums[lowest]:
                l = p+1
                p = (-1 * ((-(r-l)) // 2)) + l
            else:
                lowest = p
                r = p-1
                p = (-1 * ((-(r-l)) // 2)) + l
            if l == r == 0:
                p = 0
                if nums[p] < nums[lowest]:
                    lowest = p
                break
        return nums[lowest]