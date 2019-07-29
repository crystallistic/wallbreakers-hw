class Solution:
    def exist(self, board, word):
        if not board: return False
        path = ''
        ans = False

        # using dfs and backtracking
        def dfs(board,row,col,path,word):
            if len(word) == len(path):
                return word == path
            if row < 0 or row > len(board)-1 or col < 0 or col > len(board[0])-1:
                return False
            if board[row][col] == -1: return False
            
            if board[row][col] != word[len(path)]: return False
            
            
            letter = board[row][col]
            path += letter
            board[row][col] = -1
            ans = dfs(board,row-1,col,path,word) or dfs(board,row+1,col,path,word) or dfs(board,row,col-1,path,word) or dfs(board,row,col+1,path,word)
            board[row][col] = letter
            return ans

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(board, row, col, path, word):
                    return True
        return False