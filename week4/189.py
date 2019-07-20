class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using queue
        if  nums and len(nums) != 1 and len(nums) != k:
        
            k = k % len(nums)
            queue = collections.deque()

            for i in range(k,0,-1):
                queue.append(nums[len(nums)-i])

            for n in range(len(nums)- k - 1,-1,-1 ):
                nums[n+k] = nums[n]

            for i in range(k):
                nums[i] = queue.popleft()
        
        
        