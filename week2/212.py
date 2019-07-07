class TrieNode(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.isWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()    
            curr = curr.children[char]
        curr.isWord = True

    
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        root = TrieNode()
        
        # insert word into trie
        for word in words:
            root.insert(word)
            
        ans = []
            
        # dfs
        for row in range(len(board)):
            for col in range(len(board[row])): 
                    self.dfs(board, row, col, root,"", ans)
        return ans
    
    def dfs(self,board,row,col,trieNode,path, ans):
        
        if trieNode.isWord:
            ans.append(path)
            trieNode.isWord = False
        
        self.height = len(board)
        self.width = len(board[0])
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return
        
        letter = board[row][col]
        if letter not in trieNode.children:
            return
        
        trieNode = trieNode.children[letter]
        
        board[row][col] = "."
        
        self.dfs(board,row+1,col,trieNode,path+letter,ans)
        self.dfs(board,row-1,col,trieNode,path+letter,ans)
        self.dfs(board,row,col+1,trieNode,path+letter,ans)
        self.dfs(board,row,col-1,trieNode,path+letter,ans)
        
        board[row][col] = letter