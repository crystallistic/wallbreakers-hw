class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        i, j = 0,0
        gs, ss = sorted(g), sorted(s)
          
        while i < len(g) and j < len(s):
            # if greed <= size
            if gs[i] <= ss[j]:
                i += 1
            j += 1
        return i