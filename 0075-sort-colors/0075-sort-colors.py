class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c={}
        for i in range(len(nums)):
            c[nums[i]]=c.get(nums[i],0)+1
        index=0
        for j in range(3):
            fq=c.get(j,0)
            nums[index:index+fq]=[j]*fq
            index+=fq
        