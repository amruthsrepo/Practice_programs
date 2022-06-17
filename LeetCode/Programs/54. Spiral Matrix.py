class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) < 1:
            return matrix
        r,c = len(matrix), len(matrix[0])
        retMatrixLen = r*c
        retMatrix = []
        # incrI,incrJ = True,False
        # decrI,decrJ = False,False
        def insertTop():
            retMatrix.extend(matrix[0])
            del matrix[0]
        def insertBottom():
            for i in range(len(matrix[-1])-1, -1, -1):
                retMatrix.append(matrix[-1][i])
            del matrix[-1]
        def insertRight():
            for row in matrix:
                retMatrix.append(row[-1])
                del row[-1]
        def insertLeft():
            for i in range(len(matrix)-1, -1, -1):
                retMatrix.append(matrix[i][0])
                del matrix[i][0]
        while matrix and matrix[0]:
            if matrix and matrix[0]: insertTop()
            # print(retMatrix, str(matrix))
            if matrix and matrix[0]: insertRight()
            # print(retMatrix, str(matrix))
            if matrix and matrix[0]: insertBottom()
            # print(retMatrix, str(matrix))
            if matrix and matrix[0]: insertLeft()
            # print(retMatrix, str(matrix))
        return retMatrix

s = Solution()
print(s.spiralOrder([[7],[9],[6]]))
print(s.spiralOrder([[1,2,3]]))
# print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
a = [[]]
bool(a)