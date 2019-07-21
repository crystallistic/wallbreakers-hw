from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        self.backtrack(ans, [], nums, 0)
        return ans

    def backtrack(self, ans, tempList, nums, start ):

        ans.append(deepcopy(tempList))
        for i in range(start, len(nums)):
            tempList.append(nums[i])
            self.backtrack(ans, tempList, nums, i+1)
            tempList.pop()