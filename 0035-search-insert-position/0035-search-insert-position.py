class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        res=len(nums)
        while(l<=h):
            m=(l+h)//2
            if nums[m]>=target:
                res=m
                h=m-1
            else:
                l=m+1
        return res

        