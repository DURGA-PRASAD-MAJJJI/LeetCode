class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i]==target:
                return nums[i]
            elif target not in nums:
                nums.insert(i,target)