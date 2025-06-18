import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            c = {}
            for i in nums:
                c[i] = c.get(i, 0) + 1
            print(c)
            min_heap=[]
            for i in c:
                heapq.heappush(min_heap,(c[i],i))
                if len(min_heap)>k:
                    heapq.heappop(min_heap)
            result=[]
            for i,j in min_heap:
                result.append(j)
            return result
                