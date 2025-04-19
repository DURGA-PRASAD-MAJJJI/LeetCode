from bisect import bisect_left,bisect_right
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort();res=0
        for i in range(len(nums)):
            res+=bisect_right(nums,upper-nums[i],i+1)-bisect_left(nums,lower-nums[i],i+1)
        return res
