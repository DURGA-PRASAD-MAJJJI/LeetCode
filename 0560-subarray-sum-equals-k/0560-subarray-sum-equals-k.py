class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = 0
        c = 0
        f = {0: 1}
        
        for i in nums:
            pre += i
            need = pre - k

            if need in f:
                c += f[need]

            f[pre] = f.get(pre, 0) + 1

        return c
