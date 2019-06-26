class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        max = 0
        last1 = -1
        for i in range(N.bit_length()):
            if N & (1 << i):
                if max < (i - last1) and last1 >= 0:
                    max = (i - last1)
                last1 = i
        return max