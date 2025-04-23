class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        max_size = 0
        for i in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(i))
            count[digit_sum] += 1
            max_size = max(max_size, count[digit_sum])
        return sum(1 for v in count.values() if v == max_size)
