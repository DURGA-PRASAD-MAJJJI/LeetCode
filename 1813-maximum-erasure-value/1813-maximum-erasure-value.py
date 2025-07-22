class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        visit=set()
        l=0
        curr=0
        maxx=0
        for i in range(len(nums)):
            while nums[i] in visit:
                curr-=nums[l]
                visit.remove(nums[l])
                l+=1
            curr+=nums[i]
            visit.add(nums[i])
            maxx=max(maxx,curr)
        return maxx

        