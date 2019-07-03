class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words): return False
        seenValues = set()
        lookup = dict()
        for c,w in zip(pattern,words):
            if (c in lookup and lookup[c] != w) or (c not in lookup and w in seenValues):
                    return False
            else:
                lookup[c]= w
                seenValues.add(w)
        return True