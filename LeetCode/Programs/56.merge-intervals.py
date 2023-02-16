#
# @lc app=leetcode id=56 lang=python
#
# [56] Merge Intervals
#

# @lc code=start
class Solution(object):
    def merge(self, intervals):
        if len(intervals)<2:    return intervals
        intervals.sort(key= lambda x: x[0])
        retVals = []
        prevStart, prevEnd = intervals.pop(0)
        while intervals:
            start, end = intervals.pop(0)
            if start <= prevEnd:
                prevEnd = max(end,prevEnd)
            else:
                retVals.append([prevStart, prevEnd])
                prevStart,prevEnd = start, end
        if not retVals or prevEnd != retVals[-1][-1]:
            retVals.append([prevStart, prevEnd])
        return retVals

        
# @lc code=end

