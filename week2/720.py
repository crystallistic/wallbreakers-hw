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

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        # dfs using a stack. Store (trieNode,level) in stack.
        stack = [(trie,0)]
        longest = []    
        maxHeight = 0
        
        while stack:
            curr = stack.pop()
            
            node, height= curr[0], curr[1]
            
            # push the node's children onto the stack whose values != None
            # because we want to find the longest word that can be built 
            # one character at a time by other words in words.
            # In a trie, these words form continuous branches where no node has value None.
            if node.children:
                for child in node.children:
                    if node.children[child].val != None:
                        stack.append((node.children[child],height+1))
           
            # keep a list of the longest words 
            if height >= maxHeight:
                if height > maxHeight:
                    longest = []
                    maxHeight = height
                longest.append(node.val)
        
        # return the longest word with the smallest lexicographical order
        return min(longest)
        