class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = float('inf')
        
        for index in range(len(nums) - 2):
            start, end = index + 1, len(nums) - 1
            while start < end:
                temp_sum = nums[index] + nums[start] + nums[end]
                if abs(temp_sum - target) < abs(result - target):
                    result = temp_sum
                if temp_sum < target:
                    start += 1
                elif temp_sum > target:
                    end -= 1
                else:
                    return temp_sum
        
        return result