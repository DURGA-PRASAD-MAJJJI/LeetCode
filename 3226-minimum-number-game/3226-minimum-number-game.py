class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        print(nums)
        li=[]
        while(len(nums)!=0):
            p=min(nums)
            # print(p)
            nums.remove(p)
            b=min(nums)
            # print(b)
            nums.remove(b)
            li.append(b)
            li.append(p)
        return li
        