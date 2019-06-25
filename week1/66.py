class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """       
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            sum = digits[i] + carry
            if sum != 10:
                carry = 0
            digits[i] = sum % 10
        
        if carry == 1:
            return [1] + [0]*len(digits)
        
        return digits