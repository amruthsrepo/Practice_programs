class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxL,maxR = height[0],height[-1]
        lPtr,rPtr = 0,len(height)-1
        totalWater = 0
        #while left<right
        while lPtr<rPtr:
            # if maxL<=maxR, incr lPtr, add maxL-height[lPtr] to total, update maxL
            if maxL<=maxR:
                lPtr += 1
                totalWater += max(maxL-height[lPtr],0)
                maxL = max(maxL,height[lPtr])
            # else, decr rPtr, add maxR-height[rPtr] to total, update rPtr
            else:
                rPtr -= 1
                totalWater += max(maxR-height[rPtr],0)
                maxR = max(maxR,height[rPtr])
        return totalWater