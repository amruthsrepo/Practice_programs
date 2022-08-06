def gridTraveler(m,n):
    grid = [ [ 0 for _i in range(n) ] for _j in range(m) ]
    m -= 1
    n -= 1
    for nInd in range(n, -1, -1):
        grid[m][nInd] = 1
    for mInd in range(m, -1, -1):
        grid[mInd][n] = 1
    grid[m][n] = 0
    m -= 1
    n -= 1
    while True:
        for nInd in range(n, -1, -1):
            grid[m][nInd] = grid[m+1][nInd] + grid[m][nInd+1]
        for mInd in range(m, -1, -1):
            grid[mInd][n] = grid[mInd+1][n] + grid[mInd][n+1]
        m -= 1
        n -= 1
        m = m if m > -1 else 0
        n = n if n > -1 else 0
        if m == 0 and n == 0:
            break
    # print(grid)
    print(grid[0][1] + grid[1][0])

gridTraveler(4,5)
gridTraveler(3,3)
gridTraveler(18,18)