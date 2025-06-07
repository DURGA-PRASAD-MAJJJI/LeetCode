class Solution(object):
    def climbStairs(self, n):
        if n==1:
            return 1
        x,y=1,2
        for _ in range(n-2):
            x,y=y,x+y
        return y
