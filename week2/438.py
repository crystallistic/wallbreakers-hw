class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        ans = []
        ls,lp = len(s), len(p)
        if ls - lp < 0: return ans
        cp = collections.Counter(p)
        cs = collections.Counter(s[:lp-1])
        
            
        for i in range(lp-1, ls):   
            cs[s[i]] += 1
            
            if cs == cp:
                ans.append(i-lp + 1)
                
            cs[s[i-lp + 1]] -= 1
            if cs[s[i-lp + 1]] == 0:
                del cs[s[i-lp + 1]] 
              
        return ans

""" 
faster solution using defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        
        ans = []
        ls,lp = len(s), len(p)
        if ls - lp < 0: return ans
        
        cp = collections.defaultdict(int)
        for c in p:
            cp[c] += 1
            
        cs = collections.defaultdict(int)
        for i in range(lp-1):
            cs[s[i]] += 1
                     
        for i in range(lp-1, ls):   
            cs[s[i]] += 1
            
            if cs == cp:
                ans.append(i-lp + 1)
                
            cs[s[i-lp + 1]] -= 1
            if cs[s[i-lp + 1]] == 0:
                del cs[s[i-lp + 1]] 
              
        return ans
"""