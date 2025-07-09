class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        res=sorted(d.keys())
        m={}
        n=len(res)
        def fun(i):
            if i>=n:
                return 0
            if i in m:
                return m[i]
            ans=res[i]*d[res[i]]
            if i + 1 < n and res[i + 1] == res[i] + 1:
                take = ans + fun(i + 2)
            else:
                take=ans+fun(i+1)
            skip=fun(i+1)
            m[i]=max(take,skip)
            return m[i]
        return fun(0)

