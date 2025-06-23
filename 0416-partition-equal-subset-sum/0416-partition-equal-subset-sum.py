class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        self.dd = [[-1]*(target+1) for _ in range(n+1)]
        for i in range(n+1):
            self.dd[i][0] = True
        return self.solve(nums,target,n)
    def solve(self,nums,target,n):
        if n==0:
            return False
        if target==0:
            return True
        if self.dd[n][target]!=-1:
            return self.dd[n][target]
        if nums[n-1]<=target:
            inc=self.solve(nums,target-nums[n-1],n-1)
            exc=self.solve(nums,target,n-1)
            self.dd[n][target]=inc or exc
        else:
            self.dd[n][target]=self.solve(nums,target,n-1)
        return self.dd[n][target]