class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0]:
            return False
        row = -1
        while row < len(matrix)-1 and matrix[row+1][0] <= target:
            row += 1
        row = matrix[row]
        if target > row[-1]:
            return False
        l,r = 0,len(row)-1
        p = r/2
        i = 0
        while row[p] != target and l < r:
            i += 1
            print(p, l, r)
            if row[p] > target:
                r = p - 1
            else:
                l = p + 1
            p = l + ((r - l) / 2)
        if row[p] != target:
            return False
        return True

s = Solution()
print(s.searchMatrix([[1]], 1))
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))