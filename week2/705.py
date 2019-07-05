class MyHashSet(object):
    """
    HashSet implementation with Python list. 
    Collision resolution using chaining.
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.initCap = 17
        self.loadingFact = 0.75
        self.elements = [0] * self.initCap
        self.capacity = self.initCap
        self.len = 0

    def hashcode(self,key):
        return key % self.capacity
    
    def resize(self):
        self.capacity <<= 1
        self.len = 0
        oldSet = copy.deepcopy(self.elements)
        self.elements = [None for _ in range(self.capacity)]
        
        for bucket in oldSet:
            if bucket:
                for elem in bucket:
                    self.add(key)
                    
        
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        loc = self.hashcode(key)
        
        if not self.elements[loc]:
            self.elements[loc] = []
        
        for elem in self.elements[loc]:
            if elem == key:
                return
        self.elements[loc].append(key)   
        self.len += 1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        loc = self.hashcode(key)
        
        if not self.elements[loc]:
            return
        
        for elem in self.elements[loc]:
            if elem == key:
                self.elements[loc].remove(key)  
                self.len -= 1
                return       

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        loc = self.hashcode(key)
        
        if not self.elements[loc]:
            return
        return (key in self.elements[loc])