class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A == None or len(A) == 0: return A
        
        ans = [[0] * len(A) for i in range(len(A[0]))]
        
        
        for row in range(len(ans)):
            for i in range(len(ans[row])):
                ans[row][i] = A[i][row]
        return ans