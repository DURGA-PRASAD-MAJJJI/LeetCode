class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c={}
        for i in s:
            c[i]=c.get(i,0)+1
            if c[i]==2:
                return i            

        