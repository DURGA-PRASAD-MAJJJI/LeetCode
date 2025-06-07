class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        root=[]
        visit=[False]*len(nums)
        def BackTracking():
            if len(root)==len(nums):
                res.append(root[:])
                # print(root[:])
                return
            for i in range(len(nums)):
                if not visit[i]:
                    visit[i]=True
                    root.append(nums[i])
                    BackTracking()
                    root.pop()
                    visit[i]=False
        BackTracking()
        return res
