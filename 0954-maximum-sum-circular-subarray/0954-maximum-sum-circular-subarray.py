class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = float("-inf")
        summ = 0

        # normal Kadane's for max subarray
        for i in range(n):
            summ = summ + nums[i]
            if summ > maxx:
                maxx = summ
            if summ < 0:
                summ = 0

        # now compute min subarray sum (Kadane's variant)
        minn = float("inf")
        summ = 0
        total = 0
        for i in range(n):
            total += nums[i]
            summ = summ + nums[i]
            if summ < minn:
                minn = summ
            if summ > 0:
                summ = 0

        # if all numbers are negative, maxx is the answer
        if maxx < 0:
            return maxx

        # otherwise take max of normal vs circular
        return max(maxx, total - minn)
