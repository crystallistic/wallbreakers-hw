def isValidSudoku(board):
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
                if val in rows[row] or val in cols[col]:
                    return False
                else:
                    rows[row].add(val)
                    cols[col].add(val)
                    
                if val in boxes[row//3][col//3]:
                    return False
                else:
                    boxes[row//3][col//3].add(val)
    
    return True