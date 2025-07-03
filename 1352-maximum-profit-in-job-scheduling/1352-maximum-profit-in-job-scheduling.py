class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs=list(zip(startTime,endTime,profit))
        jobs.sort(key=lambda x: x[1])
        n=len(jobs)
        e=[0]*n
        for i in range(n):
            e[i]=jobs[i][1]
        d=[0]*(n+1)
        for i in range(1,n+1):
            a,b,c=jobs[i-1]
            l=0
            h=n
            idx=0
            while l<h:
                m=(l+h)//2
                if e[m]<=a:
                    idx=m+1
                    l=m+1
                else:
                    h=m
            d[i]=max(d[i-1],d[idx]+c)
        return d[n]


        