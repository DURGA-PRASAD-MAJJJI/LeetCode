class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n1 = [int(d) for d in str(n)]
        summ=0
        for i in range (len(n1)):
            if i%2==0:
                summ+=n1[i]
            else:
                summ-=n1[i]
        return summ
            