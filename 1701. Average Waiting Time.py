class Solution:
    def averageWaitingTime(self, customers) -> float:
        totalWaitTime, lastFinishedAt = customers[0][1], \
            customers[0][0] + customers[0][1]
        for c in range(1, len(customers)):
            if lastFinishedAt >= customers[c][0]:
                lastFinishedAt += customers[c][1]
                totalWaitTime += lastFinishedAt - customers[c][0]
            else:
                lastFinishedAt = customers[c][0] + customers[c][1]
                totalWaitTime += customers[c][1]
        return totalWaitTime/len(customers)


s = Solution()
print(f'5: {s.averageWaitingTime([[1,2],[2,5],[4,3]])}')
print(f'3.25: {s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]])}')
