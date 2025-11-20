class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        a,b=0,0
        c=0
        while (a<len(g) and b<len(s)):
            if s[b]>=g[a]:
                c+=1
                a+=1
            b+=1
        return c
        