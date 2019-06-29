class Solution(object):
    
  def isPartOfIsland(self,grid,row,col):
    # check left > up > right > down
    """
    :rtype: tuple (row,col)
    """
    # convert into global variables
    width = len(grid[0])
    height = len(grid)

    if row < 0 or row >= height or col < 0 or col >= width or grid[row][col] != "1":
      return

    grid[row][col] = "0"

    self.isPartOfIsland(grid,row,col-1)
    self.isPartOfIsland(grid,row-1,col)
    self.isPartOfIsland(grid,row+1,col)
    self.isPartOfIsland(grid,row,col+1)


  def numIslands(self,grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    count = 0
    for row in range(len(grid)):
      for col in range(len(grid[row])):
        if grid[row][col] == "1":
          count += 1
          self.isPartOfIsland(grid,row,col)
    return count

