class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxx=nums[0]
        minn=nums[0]
        res=nums[0]
        for i in range(1,n):
            x=nums[i]
            if x<0:
                maxx,minn=minn,maxx
            maxx=max(x,maxx*x)
            minn=min(x,minn*x)
            res=max(res,maxx)
        return res