class Solution:
    def divide(self,a:int,b:int)->int:
        if a==-2**31 and b==-1:return 2**31-1
        neg=(a<0)^(b<0)
        x,y=abs(a),abs(b)
        res=0
        while x>=y:
            tmp,cnt=y,1
            while x>=(tmp<<1):
                tmp<<=1
                cnt<<=1
            x-=tmp
            res+=cnt
        return -res if neg else res