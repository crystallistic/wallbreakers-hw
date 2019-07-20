class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # Since candies must be distributed equally in number 
        # to brother and sister, the maximum number of kinds of candies 
        # the sister could gain is half the total number of candies
        
        return min(len(candies)/2,len(set(candies)))