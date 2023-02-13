class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        return ((high-low)//2)+(1 if low%2!=0 or high%2!=0 else 0)