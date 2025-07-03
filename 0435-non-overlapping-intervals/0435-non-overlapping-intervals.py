class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n=len(intervals)
        print(intervals)
        end=intervals[0][1]
        c=1
        print(end)
        for i in range(1,n):
            if intervals[i][0]>=end:
                c+=1
                end=intervals[i][1]
        return n-c
            
        