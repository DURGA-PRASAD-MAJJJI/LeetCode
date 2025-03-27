class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        c = 0
        n = c
        li = []
        for i in range(1,int(num ** 0.5) + 1): 
            if num % i == 0:
                li.append(i)
                c += i
                if i != 1 and i != num // i:
                    li.append(num // i)
                    c += num // i
        return c==num
        