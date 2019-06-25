class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ""
        k = 0
        cont = True
        lookup = dict()
        while cont and k < len(strs[0]):
            c = strs[0][k]
            
            for i in range(1, len(strs)):
                if k >= len(strs[i]) or strs[i][k] != c:
                    cont = False
                    break     
            if cont:
                lookup[k] = c
            k += 1
        
        k = 0
        ans = ""
        while k in lookup:
            ans += strs[0][k]
            k += 1
        return ans