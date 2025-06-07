class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        visit=[False]*len(nums)
        root=[]
        def BT():
            if len(nums)==len(root):
                res.append(root[:])
            for i in range(len(nums)):
                if not visit[i]:
                    visit[i]=True
                    root.append(nums[i])
                    BT()
                    root.pop()
                    visit[i]=False
        BT()
        return list(map(list, set(map(tuple, res))))
        