class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0,float('-inf'))
        nums.append(float('-inf'))
        l=0
        h=len(nums)-1
        while (l<=h):
            mid=(l+h)//2
            if nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                return mid-1
            elif nums[mid-1]>nums[mid]:
                h=mid-1
            elif nums[mid+1]>nums[mid]:
                l=mid+1        