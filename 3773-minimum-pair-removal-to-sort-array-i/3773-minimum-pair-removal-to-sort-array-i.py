class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        r = sorted(nums)
        print(r)
        c, n = 0, 0
        for i in range(len(nums)):
            if nums[i] == r[i]:
                c += 1

        if c == len(nums):
            return 0
        else:
            while True:
                if all(nums[i] >= nums[i - 1] for i in range(1, len(nums))):
                    break

                min_sum = float('inf')
                min_index = 0

                for i in range(len(nums) - 1):
                    s = nums[i] + nums[i + 1]
                    if s < min_sum:
                        min_sum = s
                        min_index = i

                res = nums[min_index] + nums[min_index + 1]
                nums.pop(min_index)
                nums.pop(min_index)
                nums.insert(min_index, res)
                print(res)
                n += 1

            print(nums)
            return n
