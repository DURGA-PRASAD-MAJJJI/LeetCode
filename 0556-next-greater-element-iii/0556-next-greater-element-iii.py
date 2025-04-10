class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))
        i = len(l) - 2
        while i >= 0 and l[i] >= l[i + 1]:
            i -= 1
        if i == -1:
            return -1
        j = len(l) - 1
        while l[j] <= l[i]:
            j -= 1
        l[i], l[j] = l[j], l[i]
        l[i + 1:] = reversed(l[i + 1:])
        res = int(''.join(l))
        return res if res <= 2**31 - 1 else -1
