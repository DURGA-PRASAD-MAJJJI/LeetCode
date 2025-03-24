class Solution:
    def minimumChairs(self, s: str) -> int:
        a=0
        l=list(s)
        l1=[]
        for i in range(len(l)):
            if (l[i]=='E'):
                a+=1
                l1.append(a)
            elif (l[i]=='L'):
                a-=1
                l1.append(a)
        return max(l1)