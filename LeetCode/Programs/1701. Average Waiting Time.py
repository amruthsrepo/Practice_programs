class Solution:
    def averageWaitingTime(self, customers) -> float:
        customers[0][0] += customers[0][1]
        for c in range(1, len(customers)):
            if customers[0][0] >= customers[c][0]:
                customers[0][0] += customers[c][1]
                customers[0][1] += customers[0][0] - customers[c][0]
            else:
                customers[0][0] = customers[c][0] + customers[c][1]
                customers[0][1] += customers[c][1]
        return customers[0][1]/len(customers)


s = Solution()
print(f'5: {s.averageWaitingTime([[1,2],[2,5],[4,3]])}')
print(f'3.25: {s.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]])}')
