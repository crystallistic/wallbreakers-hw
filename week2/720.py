class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = dict()
        self.val = None

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            
            curr = curr.children[char]
        curr.val = word

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        
        curr = self
        for char in word:
            if char not in curr.children:
                return False
    
            curr = curr.children[char]
        
        if curr.val == word:
            return True
        return False
                  

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self        
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # pre-order traversal
      
        stack = [(trie,0)]
        longest = []    
        maxHeight = 0
        
        while stack:
            curr = stack.pop()
            
            node, height= curr[0], curr[1]
            
            if node.children:
                for child in node.children:
                    if node.children[child].val != None:
                        stack.append((node.children[child],height+1))
           

            if height >= maxHeight:
                if height > maxHeight:
                    longest = []
                    maxHeight = height
                longest.append(node.val)
        
        return min(longest)