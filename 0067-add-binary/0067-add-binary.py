class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n=int(a,2)
        m=int(b,2)
        res=n+m
        result=bin(res)[2:]
        return result
       