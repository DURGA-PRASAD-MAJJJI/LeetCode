class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        self.dd=[-1 for _ in range(n+1)]
        return self.solve(nums,n-1)
    def solve(self,nums,i):
        if i<0:
            return 0
        if self.dd[i]!=-1:
            return self.dd[i]
        inc=nums[i]+self.solve(nums,i-2)
        exc=self.solve(nums,i-1)
        self.dd[i]=max(inc,exc)
        return self.dd[i]
        