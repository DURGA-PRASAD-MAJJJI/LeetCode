class Solution:
    def reverseVowels(self, s: str) -> str:
        l=list(s)
        a=0
        b=len(l)-1
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        while a<b:
            if l[a] in v and l[b] in v:
                l[a],l[b]=l[b],l[a]
                a+=1
                b-=1
            elif l[a] not in v:
                a+=1
            elif l[b] not in v:
                b-=1
        return ''.join(l)
