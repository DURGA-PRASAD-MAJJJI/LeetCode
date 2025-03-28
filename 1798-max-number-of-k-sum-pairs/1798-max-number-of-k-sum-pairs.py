from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        a = 0
        b = len(nums)-1
        while a<b:
            if a != b:
                r = nums[a] + nums[b]
                if r == k:
                    c += 1
                    a += 1
                    b -= 1
                elif r < k:
                    a += 1
                else:
                    b -= 1
        return c
