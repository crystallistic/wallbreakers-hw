class Solution:
    def myPow(self, x: float, n: int) -> float:

        cache = collections.defaultdict(int)
        cache[0] = 1
        if abs(n) >= 1:
            cache[1] = (x if n>0 else 1/x)
        return self.worker(x,n,cache)

    def worker(self,x,n,cache):

        index = abs(n)

        if cache[index] != 0:
            return cache[index]
        val = self.worker(x,index//2,cache)
        cache[index] = val * (val if not (index % 2) else self.worker(x, index - index//2,cache))
        return cache[index]