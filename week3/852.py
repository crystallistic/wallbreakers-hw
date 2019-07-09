class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        begin, end = 0, len(A) - 1
        
        while (begin <= end):
            mid = (begin + end) // 2
            
            # return peak if found
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            # if middle number is on left slope,
            # search on right half of list
            elif A[mid-1] < A[mid] and A[mid] < A[mid+1]:
                begin = mid + 1
            # if middle number is on right slope,
            # search on left half of list
            else:
                end = mid - 1