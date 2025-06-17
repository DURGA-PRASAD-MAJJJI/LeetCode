from typing import List

class Solution:
    def build(self, arr, tree, node, start, end):
        if start == end:
            tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, tree, 2 * node + 1, start, mid)
            self.build(arr, tree, 2 * node + 2, mid + 1, end)
            tree[node] = tree[2 * node + 1] ^ tree[2 * node + 2]

    def query(self, tree, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return tree[node]
        mid = (start + end) // 2
        left = self.query(tree, 2 * node + 1, start, mid, l, r)
        right = self.query(tree, 2 * node + 2, mid + 1, end, l, r)
        return left ^ right

    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        tree = [0] * (4 * n)
        self.build(arr, tree, 0, 0, n - 1)
        return [self.query(tree, 0, 0, n - 1, l, r) for l, r in queries]
