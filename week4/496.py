class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hm = dict()
        stack = []
        
        for n in nums2:
        
            while stack and n > stack[-1]:
                hm[stack.pop()] = n
            stack.append(n)
                
        while stack:
            hm[stack.pop()] = -1
        
        return [hm[e] for e in nums1]