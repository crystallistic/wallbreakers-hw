class Solution:
    def islandPerimeter(self,grid):
        if not grid: return 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return self.dfs(grid,row,col)
        return 0
    
    def dfs(self,grid,row,col):
        # if exceeding grid borders
        if row < 0 or row > len(grid)-1 or col < 0 or col > len(grid[0]) - 1:
            return 1

        # if visited
        if grid[row][col] == -1:
            return 0
        
        # fds;
        if grid[row][col] == 0:
            return 1

        # if cell = 1
        count = 0
        grid[row][col] = -1
        count += self.dfs(grid,row+1,col)
        count += self.dfs(grid,row-1,col)
        count += self.dfs(grid,row,col+1)
        count += self.dfs(grid,row,col-1)
        
        return count