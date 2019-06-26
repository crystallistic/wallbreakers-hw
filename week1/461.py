class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y        
        count = 0
        for i in range(xor.bit_length()):
            if xor & (1 << i):
                count += 1
        return count