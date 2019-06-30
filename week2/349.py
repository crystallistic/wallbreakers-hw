class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1 = set(nums1)
        
        ans = set()
        
        for e in nums2:
            if e in s1:
                ans.add(e)
        return ans

"""
The below one-line solution also works but has bad
time-space complexity.

class Solution(object):
    def intersection(self, nums1, nums2):
        return [e for e in set(nums1) if e in set(nums2)]

"""