class Solution(object):
    
    def find(self, parent, i):
        if parent[i] == -1:
            return i
        return(self.find(parent,parent[i]))
    
    def union(self,parent,i,j):
        setI = self.find(parent,i)
        setJ = self.find(parent,j)
        if (setI != setJ):
            parent[setI] = setJ

    def findCircleNum(self,M):
        """
        :type M: List[List[int]]
        :rtype: int
        """


        parent = [-1 for _ in range(len(M))]

        for row in range(len(M)):
            for col in range(row + 1, len(M[row])):
                if M[row][col] == 1:
                    self.union(parent,row,col)

        count = 0
        for e in parent:
            if e == -1:
                count += 1
        return count