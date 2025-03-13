class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=str(n)
        li=list(s)
        return ((math.prod(int(digit) for digit in s))-(sum(int(digit) for digit in s)))
            
        