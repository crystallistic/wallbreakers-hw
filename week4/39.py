from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        self.backtrack(candidates, target, [], ans)
        return ans

    def backtrack(self,candidates,target, tempList, ans):

        if target == 0:
            ans.append(deepcopy(tempList))
        else:
            for e in candidates:
                if target < 0: break
                if not tempList or e >= tempList[-1]:
                    # choose
                    tempList.append(e)
                    # explore 
                    self.backtrack(candidates,target-e, tempList,ans)
                    # unchoose
                    tempList.pop()