class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        i=0
        visit=set()
        maxx=0
        for j in range(n):
            while s[j] in visit:
                visit.remove(s[i])
                i+=1
            visit.add(s[j])
            maxx=max(maxx,j-i+1)
        return maxx

            