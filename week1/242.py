class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) == len(t):
            lookup = dict()
            for c in s:
                if c in lookup:
                    lookup[c] = lookup[c] + 1
                else:
                    lookup[c] = 1
            
            for c in t:
                if c not in lookup or lookup[c] == 0:
                    return False
                else:
                    lookup[c] -= 1         
        else:
            return False
        
        return True