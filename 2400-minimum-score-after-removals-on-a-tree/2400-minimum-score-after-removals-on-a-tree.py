import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        g = collections.defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        sx = [0] * n
        d = [set() for _ in range(n)]

        def dfs(u, p):
            sx[u] = nums[u]
            d[u].add(u)
            for v in g[u]:
                if v != p:
                    dfs(v, u)
                    sx[u] ^= sx[v]
                    d[u].update(d[v])

        dfs(0, -1)
        tx = sx[0]
        res = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                xi = sx[i]
                xj = sx[j]
                if j in d[i]:
                    a, b, c = xj, xi ^ xj, tx ^ xi
                elif i in d[j]:
                    a, b, c = xi, xj ^ xi, tx ^ xj
                else:
                    a, b, c = xi, xj, tx ^ xi ^ xj
                res = min(res, max(a, b, c) - min(a, b, c))
        return res
