class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        numTanks = len(height)
        if numTanks < 2:
            return 0
        l,r = 0,numTanks-1
        maxArea = (min(height[l], height[r]) * (r-l))
        while l<r:
            currArea = (min(height[l], height[r]) * (r-l))
            if currArea > maxArea:
                maxArea = currArea
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxArea