class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res=time//(n-1)
        r=time%(n-1)
        if res%2==0:
            return 1+r
        else:
            return n-r
        