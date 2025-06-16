class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.BIT=[0]*(self.n+1)
        self.nums=nums[:]

        for i in range(self.n):
            self.update(i+1,nums[i])
    def update(self,i:int,val:int):
        while i<=self.n:
            self.BIT[i]+=val
            i+=i&-i
    def prefix_sum(self,i:int)->int:
        self.res=0
        while i>0:
            self.res+=self.BIT[i]
            i-=i&-i
        return self.res
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum(right+1)-self.prefix_sum(left)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)