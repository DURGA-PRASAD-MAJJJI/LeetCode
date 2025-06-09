class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxi=0
        act_max,right=0,0
        alphabets=set()
        while(right<len(s)):
            if s[right] not in alphabets:
                alphabets.add(s[right])
                maxi+=1
            else:
                k=s[right]
                right=right-1
                while(s[right]!=k):
                #   alphabets.remove(s[right])
                    right-=1
                alphabets=set()
                act_max=max(act_max,maxi)
                maxi=0
            right+=1
                
        act_max=max(act_max,maxi)
        
        return act_max


        