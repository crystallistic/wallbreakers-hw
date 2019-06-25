class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        lookup = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in lookup:
                return [lookup[target - nums[i]],i]
            lookup[nums[i]] = i
        return False