class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        # once the list is sorted, the max sum of mins is equal to the sum of
        # even-indexed numbers in the list.
        return sum(sorted(nums)[0::2])