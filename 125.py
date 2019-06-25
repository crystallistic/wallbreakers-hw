class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1: return True
        
        s = s.lower()
        left,right = 0,len(s) - 1
        
        while (left < right):
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
                
        return True