class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            yield []
        else:
            for s in self.subsets(nums[1:]):
                yield s
                yield [nums[0]] + s