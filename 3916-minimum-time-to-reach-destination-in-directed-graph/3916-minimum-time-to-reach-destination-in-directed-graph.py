import heapq
from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        for a,b,c,d in edges:graph[a].append((b,c,d))
        dal=edges
        heap=[(0,0)]
        t=[float('inf')]*n
        t[0]=0
        while heap:
            i,a=heapq.heappop(heap)
            # if a==-1:
            #     return t
            if i>t[a]:
                continue
            for b,c,d in graph[a]:
                if c<=i<=d and i+1<t[b]:
                    t[b]=i+1
                    heapq.heappush(heap,(i+1,b))
                elif i<c and c+1<t[b]:
                    t[b]=c+1
                    heapq.heappush(heap,(c+1,b))
        return t[n-1] if t[n-1]!=float('inf') else -1
                