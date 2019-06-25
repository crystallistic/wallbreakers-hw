class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = [0] * len(A)
        even, odd = 0,len(A) - 1
        
        for e in A:
            if e % 2 == 0:
                ans[even] = e
                even += 1
            else:
                ans[odd] = e
                odd -= 1
        return ans