class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first(nums,target):
            l,h=0,len(nums)-1
            f=-1
            while(l<=h):
                m=(l+h)//2
                if nums[m]==target:
                    f=m
                    h=m-1
                elif nums[m]>target:
                    h=m-1
                else:
                    l=m+1
            return f
        def last(nums,target):
            l,h=0,len(nums)-1
            e=-1
            while(l<=h):
                m=(l+h)//2
                if nums[m]==target:
                    e=m
                    l=m+1
                elif nums[m]>target:
                    h=m-1
                else:
                    l=m+1
            return e

        return [first(nums,target),last(nums,target)]