class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            dig = [int(d)for d in str(nums[i])]
            li.extend(dig)
        return li