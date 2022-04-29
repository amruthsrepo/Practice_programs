class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals):
        intervalsIndices = sorted(range(len(intervals)), key=lambda k: intervals[k].start)
        for i in range(1, len(intervals)):
            if intervals[intervalsIndices[i-1]].end > intervals[intervalsIndices[i]].start:
                return False
        return True