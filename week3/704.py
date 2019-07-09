class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        begin, end = 0, len(nums) - 1
        
        while begin <= end:
            mid = (begin + end) // 2
            
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid - 1
            else:
                begin = mid + 1
        
        return -1