class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i=0
        summ=0
        maxx=nums[0]
        while i<len(nums):
            summ+=nums[i]
            maxx=max(maxx,summ)
            if summ<0:
                summ=0
            i+=1
        return maxx
