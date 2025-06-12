class Solution:
    def minEatingSpeed(self, piles, h):
        from math import ceil
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            tot = sum(ceil(i / m) for i in piles)
            if tot > h:
                l = m + 1
            else:
                r = m - 1
        return l
