class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        groups = set()
        
        for w in A:
            even = ''.join(sorted(w[0::2]))
            odd = ''.join(sorted(w[1::2]))
            groups.add((even,odd))
        return len(groups)