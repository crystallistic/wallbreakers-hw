class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """       
        ans = []
        for num in range(left,right+1):
            k = 0
            valid = True
            while num // (10**k) > 1 and valid:
                digit = (num%10**(k+1))//(10**k)
                if digit == 0 or num % digit != 0:
                    valid = False
                k += 1
            
            if valid:
                ans.append(num)
        return ans
        