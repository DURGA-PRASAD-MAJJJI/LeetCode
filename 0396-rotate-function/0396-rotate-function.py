class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        summ=sum(nums)
        value=sum(i*nums[i] for i in range(n))
        maxx=value
        for i in range(1, n):
            value=value + summ - n * nums[-i]
            maxx=max(maxx,value)
        return maxx
