class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        li=[]
        for i in range(len(nums)):
            r=list(bin(nums[i]))
            if r[-1]=='0':
                li.append(nums[i])
        print(li,len(li))
        if len(li)<2:
            return False
        else:
            res=list(bin(sum(li)))
            print(res)
            if res[-1]=='0':
                return True
            else:
                return False