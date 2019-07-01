class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        ct = collections.Counter(t)
        
        for c in s:
            ct.update({c:-1})
            if ct[c] == 0:
                del ct[c]
                
        ans = ""
        for e in ct:
            ans = e
        return ans

"""
Alternate solution using defaultdict

class Solution(object):
    def findTheDifference(self, s, t):
        
        ct = collections.defaultdict(int)
        
        for c in t:
            ct[c] += 1
        
        for c in s:
            ct[c] -= 1
            if ct[c] == 0:
                del ct[c]
                
        ans = ""
        for e in ct:
            ans = e
        return ans
"""