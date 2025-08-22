class Solution:
    def maxSubarraySumCircular(self, a: List[int]) -> int:
        b = sum(a)
        c = d = e = f = a[0]
        for g in a[1:]:
            d = max(g, d + g)
            c = max(c, d)
            f = min(g, f + g)
            e = min(e, f)
        if c < 0:
            return c
        return max(c, b - e)
