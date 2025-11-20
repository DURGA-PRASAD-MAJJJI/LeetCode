class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        maxx=0
        ss=set()
        for k in range(len(s)):
            while s[k] in ss:
                ss.remove(s[i])
                i+=1
            ss.add(s[k])
            maxx=max(maxx,k-i+1)
        return maxx