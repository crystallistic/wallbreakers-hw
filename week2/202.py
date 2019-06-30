class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        seen = set()


        while n not in seen:
            seen.add(n)

            # extract digits from number n
            k = int(math.log(n,10))
            digitsSq = [0] * (k+1) #squares of each digit
            while k > -1:
                digitSq = ((n // (10**k)) % 10) ** 2 # extract digit and square it
                digitsSq[k] = digitSq
                k -= 1
            n = sum(digitsSq)
            if n == 1:
                return True
        
        # if a value of n is already seen, then the original value of n is not a happy number
        return False