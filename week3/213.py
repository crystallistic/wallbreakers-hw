class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []: return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        
        # keep track of prev and previous prev possibilities
        # tuple = (sum if robbbing first, sum if robbing last)
        first, second = (nums[0],0),(max(nums[1],nums[0]),nums[1])
        
        # same logic as house robber 1 question
        # choose max value between previous sum and sum of current
        # house's stash with sum of prevprev sum
        for h in range(2, len(nums)):
            withBegin = max(first[0] + nums[h], second[0])
            withEnd = max(first[1] + nums[h], second[1])
            first = second
            second = (withBegin,withEnd)
        
        # compare sum of robbing first house and robbding last house
        return max(second[1],first[0])