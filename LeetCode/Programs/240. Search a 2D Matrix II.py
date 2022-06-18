class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        l,r,t,b = -1,len(matrix[0])-1,-1,len(matrix)-1
        rowCol1 = 0
        # print(l,r,t,b)
        while rowCol1<=r and rowCol1<=b and matrix[rowCol1][rowCol1] < target:
            rowCol1 += 1
        while l < r-1 and matrix[0][l+1] < target:
            l += 1
        while l < r and matrix[0][r-1] > target:
            r -= 1
        while t < b-1 and matrix[t+1][0] < target:
            t += 1
        while t < b and matrix[b-1][0] > target:
            b -= 1
        l = min(rowCol1, l)
        t = min(rowCol1, t)
        # print(l,r,t,b)
        for row in range(t, b+1):
            lTemp,rTemp = 0,r
            p = r/2
            while lTemp < rTemp and matrix[row][p] != target:
                if matrix[row][p] > target:
                    rTemp = p - 1
                else:
                    lTemp = p + 1
                p = lTemp + ((rTemp - lTemp) / 2)
            if matrix[row][p] == target:
                return True
        for col in range(l, r+1):
            tTemp,bTemp = 0,b-1
            p = bTemp/2
            while tTemp < bTemp and matrix[p][col] != target:
                if matrix[p][col] > target:
                    bTemp = p - 1
                else:
                    tTemp = p + 1
                p = tTemp + ((bTemp - tTemp) / 2)
            if matrix[p][col] == target:
                return True
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7,9],[2,4,6,8,10],[11,13,15,17,19],[12,14,16,18,20],[21,22,23,24,25]]
,13))
print(s.searchMatrix([[1],[3],[5]]
,1))
print(s.searchMatrix([[1,4,7,11]]
,5))
print(s.searchMatrix([[1],[2],[3],[4]]
,5))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
,5))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
,19))
print(s.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
,75))