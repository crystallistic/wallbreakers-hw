class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        cs, ct = 0,0
        
        # compare character by character 
        while cs < len(s) and ct < len(t):
            if s[cs] == t[ct]:
                cs += 1
            ct += 1
        
        # return True if all string s has been traversed
        return cs == len(s)