class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        mask = 0
        for i in range(num.bit_length()):
            mask += 1 << i
        return num ^ mask

""" Or one liner: 
class Solution(object):
    def findComplement(self, num):
        return num ^ sum([1<<i for i in range(num.bit_length())])
"""