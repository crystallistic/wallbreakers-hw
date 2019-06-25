class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        
        left, right= 0, len(s)-1
        lst = list(s)
        while left <= right:
            if s[left] not in vowels:
                lst[left] = s[left]
                left += 1
            elif s[right] not in vowels:
                lst[right] = s[right]
                right -= 1
            else:
                lst[left], lst[right] = s[right],s[left]
                left += 1
                right -= 1
        
        return "".join(lst)