from heapq import heappush

def maxRow(matrix):
    l,b = len(matrix), len(matrix[0])
    rowsSet = [list() for _i in range(l)]
    colSet = [list() for _i in range(b)]
    
    for i in range(l):
        for j in range(b):
            # print(i,j,l,b, len(rowsSet), len(colSet))
            heappush(rowsSet[i], (-matrix[i][j], j))
            heappush(colSet[j], matrix[i][j])
    
    for i in range(l):
        prevRowMax = rowsSet[i][0][0]
        for j in range(b):
            rowMax,index = rowsSet[i][0]
            # print(i,j,prevRowMax,rowMax, colSet[index][0])
            if rowMax > prevRowMax:
                break
            if colSet[index][0] + rowMax == 0:
                return -rowMax
            
    return -1


a = [[1,2],[3,4]]
print(maxRow(a))
b = [[5,3,2],[1,1,2],[5,6,7]]
print(maxRow(b))