class Solution(object):
    def maxProfit(self, prices):
        maxProf = l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxProf = max(maxProf, prices[r] - prices[l])
        return maxProf