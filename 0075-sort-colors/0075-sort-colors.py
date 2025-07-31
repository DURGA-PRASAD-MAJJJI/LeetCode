class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            mini=i
            for j in range(i+1,n):
                if nums[mini]>nums[j]:
                    mini=j
            temp=nums[mini]
            nums[mini]=nums[i]
            nums[i]=temp 
