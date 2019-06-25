class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
             
        return [s[i] for i in range(len(s)-1,-1,-1)]