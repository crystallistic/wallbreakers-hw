class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []: return 0
        if len(nums) <= 2: return max(nums)
        
        
        # same-ish logic as house robber I, but using cache
        def recursion(begin,end,cache):
            
            if end in cache:
                return cache[end]
            
            if begin == end:
                return nums[begin]
            if begin == end -1:
                return max(nums[begin],nums[end])
            
            cache[end] =  max(recursion(begin,end-2,cache) + nums[end],recursion(begin,end-1,cache))
                              
            return cache[end]
        
        # compare sum of robbing first house (not last house)
        # and robbing last house (not first house)
        return max(recursion(0,len(nums)-2,dict()),recursion(1,len(nums)-1,dict()))