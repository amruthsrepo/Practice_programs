from typing import List
class Solution:
    def __init__(self):
        self.lis = [1,2,1]
    def getRowUtil(self, i):
        self.lis.insert((i), (self.lis[i] + self.lis[i-1]))
        for j in range((i-1),0,-1):
            self.lis.insert((j), (self.lis[j] + self.lis[j-1]))
            del self.lis[j+1]
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        elif rowIndex == 2:
            return self.lis
        else:
            for k in range(2,rowIndex):
                self.getRowUtil(k)
            return self.lis

if __name__ == "__main__":
    sol = Solution()
    op = sol.getRow(3)
    print(op)
