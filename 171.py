class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        sum = 0
        k = len(s) - 1
        for c in s:
            sum += (ord(c) - 64) * (26**k) 
            k -= 1
        return sum