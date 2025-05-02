class Solution:
    def rob(self, nums: List[int]) -> int:
        a,b=0,0
        for i in nums:
            t=max(a,b+i)
            b=a
            a=t
        return a


        