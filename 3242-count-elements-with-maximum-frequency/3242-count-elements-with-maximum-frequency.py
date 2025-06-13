class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c={}
        for i in nums:
          c[i]=c.get(i,0)+1
        l=list(c.values())
        res=0
        for i in range(len(l)):
            print(l[i])
            if l[i]==max(l):
                res+=l[i]
        return res
        