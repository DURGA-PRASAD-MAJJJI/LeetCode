class Solution:
    def rob(self, nums: List[int]) -> int:
        global d
        d={}
        i=0
        n=len(nums)
        if len(nums)<2:
            return nums[i]
        inc=self.fun(nums,d,n-2,i)
        d={}
        exc=self.fun(nums,d,n-1,i+1)
        return max(inc,exc)
    def fun(self,nums,d,n,i):
        if i>n:
            return 0
        if i in d:
            return d[i]
        a=nums[i]+self.fun(nums,d,n,i+2)
        b=self.fun(nums,d,n,i+1)
        d[i]=max(a,b)
        return d[i]