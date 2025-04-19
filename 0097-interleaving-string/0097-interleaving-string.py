class Solution:
    def isInterleave(self, a: str, b: str, c: str) -> bool:
        x,y=len(a),len(b)
        if x+y!=len(c):return False
        d=[False]*(y+1)
        d[0]=True
        for j in range(1,y+1):
            d[j]=d[j-1] and b[j-1]==c[j-1]
        for i in range(1,x+1):
            d[0]=d[0] and a[i-1]==c[i-1]
            for j in range(1,y+1):
                d[j]=(d[j] and a[i-1]==c[i+j-1]) or (d[j-1] and b[j-1]==c[i+j-1])
        return d[y]
