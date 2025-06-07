class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        l=list(range(1,n+1))
        return list(combinations(l,k))
