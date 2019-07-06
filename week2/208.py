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


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)