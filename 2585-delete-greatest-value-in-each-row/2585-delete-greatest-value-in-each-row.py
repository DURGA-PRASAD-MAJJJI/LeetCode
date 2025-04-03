class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        l=[]
        while any(grid):
            li=[]
            for i in grid:
                if i:
                    m=max(i)
                    li.append(m)
                    i.remove(m)
            l.append(max(li))
        return sum(l)
        