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
            # return target if equal to middle number
            if nums[mid] == target:
                return mid
            # if target < middle number, then search in left haft of list
            elif target < nums[mid]:
                end = mid - 1
            # else search in right half
            else:
                begin = mid + 1       
        return -1