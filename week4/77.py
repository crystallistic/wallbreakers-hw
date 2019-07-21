from copy import deepcopy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
    
        ans = []
        self.backtrack(ans,[],n,k,1)
        return ans

    def backtrack(self,ans,tempList,n,k,start):
        # if tempList is long enough
        if len(tempList) == k:
            ans.append(deepcopy(tempList))
        else:
            for i in range(start,n+1):
                if not tempList or i > tempList[-1]:
                    #choose
                    tempList.append(i)
                    #explore
                    self.backtrack(ans,tempList,n,k,start+1)
                    #unchoose
                    tempList.pop()