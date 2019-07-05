class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        width = len(board)
        rows = {i:set() for i in range(width)}
        cols = {j:set() for j in range(width)}
        boxes = [[set() for _ in range(width//3)] for _ in range((width//3))]
        # check 
        for row in range(width):
            for col in range(width):
                val = board[row][col]
                if val != '.':
                    if val in rows[row] or val in cols[col] or val in boxes[row//3][col//3]:
                        return False
                    else:
                        rows[row].add(val)
                        cols[col].add(val)
                        boxes[row//3][col//3].add(val)        
        return True    

"""

Faster solution with one set:

class Solution(object):
    def isValidSudoku(self, board):

        width = len(board)
        seen = set()
        # check 
        for row in range(width):
            for col in range(width):
                val = board[row][col]
                if val != '.':
                    if (row,val) in seen or (val,col) in seen or (row//3,col//3,val) in seen:
                        return False
                    else:
                        seen.add((row,val))
                        seen.add((val,col))
                        seen.add((row//3,col//3,val))        
        return True    

"""