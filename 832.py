class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        for i in range(len(A)):
            for j in range(len(A[i])//2):
                A[i][j], A[i][len(A[i])-1-j] = A[i][len(A[i])-1-j], A[i][j]
                
        for i in range(len(A)):
            for j in range(len(A[i])):
                
                A[i][j] = (0 if A[i][j] == 1 else 1)
                
        return A