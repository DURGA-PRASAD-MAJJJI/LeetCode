class Solution:
    def isSameTree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val == b.val:
            return self.isSameTree(a.left, b.left) and self.isSameTree(a.right, b.right)
        return False