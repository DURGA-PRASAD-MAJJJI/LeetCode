class Solution:
    def reorganizeString(self, s: str) -> str:
        r = Counter(s)
        m = max(r.items(), key=lambda x: x[1])
        a=m[1]
        b=(len(s)+1)//2
        l=['']*len(s)
    
        if a>b:
            return ""
        r = sorted(r.items(), key=lambda x: -x[1])
        i = 0
        for j, k in r:
            for _ in range(k):
                if i >= len(s):
                    i = 1
                l[i] = j
                i += 2
        return ''.join(l)


        