class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        k = 0
        while 2 ** k < n:
            k += 1
        return (2**k) == n