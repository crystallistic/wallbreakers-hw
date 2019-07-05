class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        mappings = dict()
        
        for i,j in zip(s,t):
            if (i in mappings and (mappings[i] != j )) or (i not in mappings and j in mappings.values()):
                return False
            
            mappings[i] = j
            
            
        return True