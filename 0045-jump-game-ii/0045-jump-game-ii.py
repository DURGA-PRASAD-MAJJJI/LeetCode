class Solution:
    def jump(self, nums: List[int]) -> int:
        c=0
        max_jump=0
        curr_jump=0
        for i in range(len(nums)-1):
            max_jump=max(max_jump,i+nums[i])
            if i==curr_jump:
                c+=1
                curr_jump=max_jump
        return c
