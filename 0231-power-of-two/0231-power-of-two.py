class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        c=0
        while n:
            c+=(n&1)
            n=n>>1
        print(c)
        if c==1:
            return True
        else:
            return False
            