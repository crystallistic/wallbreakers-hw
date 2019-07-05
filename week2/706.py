class Node(object):
    
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
    
    def getKey(self):
        return self.key
    
    def getValue(self):
        return self.value
    
    def setValue(self,value):
        self.value = value
        
    
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.initCap = 15000
        self.loadingFact = 0.75
        self.pairs = [None] * self.initCap
        self.len = 0
        self.capacity = self.initCap
    
    def hashcode(self,key):
        return key % self.capacity
    
    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        
        # resize hashmap if needed
        if self.len + 1 > self.loadingFact * self.capacity:
            self.resize()
                
        posLoc = self.hashcode(key)
        node = self.pairs[posLoc]
        
        # if bucket is empty, insert key-value pair
        if node == None:
            self.pairs[posLoc] = Node(key,value)
            self.len += 1
            return
        
        # if bucket is occupied, insert by chaining
        prev = node
        while node != None: 
            if node.getKey() == key:
                node.setValue(value)
                return
            prev = node
            node = node.next
        node = Node(key,value)
        prev.next = node
        self.len += 1
                
    
    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        posLoc = self.hashcode(key)
        node = self.pairs[posLoc]
        if node == None: return -1
        
        while node != None:
            if node.getKey() == key:
                return node.getValue()
            node = node.next
        return -1
                
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        
        posLoc = self.hashcode(key)
        node = self.pairs[posLoc]
        
        if node != None:
            if node.getKey() == key:
                self.pairs[posLoc] = node.next
                self.len -= 1
            else:
                while node.next != None:
                    if node.next.getKey() == key:
                        node.next = node.next.next
                        self.len -= 1
                        return
                    node = node.next
    
    def resize(self):
        self.capacity <<= 1
        self.len = 0
        oldHM = [] + self.pairs
        self.pairs = [None] * self.capacity
        
        for i in range(len(oldHM)):
            if oldHM[i] != None:
                node = oldHM[i]
                while node != None:
                    loc = self.hashcode(node.getKey())
                    self.pairs[loc] = node
                    self.len += 1
                    node = node.next