from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        self.backtrack(ans, [], nums)
        return ans

    def backtrack(self, ans, tempList, nums):

        if len(tempList) == len(nums):
            ans.append(deepcopy(tempList))
        else:
            for i in range(len(nums)):
                if nums[i] in tempList: continue
                # choose
                tempList.append(nums[i])

                # explore
                self.backtrack(ans,tempList,nums)
                # unchoose
                tempList.pop()