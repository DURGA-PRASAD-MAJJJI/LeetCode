class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        res=0
        for j in range(len(nums)):
            while nums[j]-nums[i]>1:
                i+=1
            if abs(nums[j]-nums[i])==1:
                res=max(res,j-i+1)
        return res

        