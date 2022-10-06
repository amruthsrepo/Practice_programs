class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.numIslandsUtil(grid, i, j)
                    count += 1
        return count

    def numIslandsUtil(self, grid, i, j):
        grid[i][j] = '2'
        if i>0 and grid[i-1][j] == '1':
            self.numIslandsUtil(grid, i-1, j)
        if i<len(grid)-1 and grid[i+1][j] == '1':
            self.numIslandsUtil(grid, i+1, j)
        if j>0 and grid[i][j-1] == '1':
            self.numIslandsUtil(grid, i, j-1)
        if j<len(grid[0])-1 and grid[i][j+1] == '1':
            self.numIslandsUtil(grid, i, j+1)