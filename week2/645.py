class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(nums)
        missing = -1
        extra = -1
        for i in range(1, len(nums) + 1):
            if i not in count:
                missing = i
            else:
                if count[i] > 1:
                    extra = i
        
        return [extra, missing]
                
                
"""
Slightly more effective solution with defaultdict

class Solution(object):
    def findErrorNums(self, nums):
        
        count = collections.defaultdict(int)
        for n in nums:
            count[n] += 1
        
        missing = -1
        extra = -1
        for i in range(1, len(nums) + 1):
            if i not in count:
                missing = i
            else:
                if count[i] > 1:
                    extra = i
        
        return [extra, missing]

"""