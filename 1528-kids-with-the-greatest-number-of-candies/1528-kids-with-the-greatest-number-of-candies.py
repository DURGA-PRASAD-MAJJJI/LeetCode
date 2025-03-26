class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        li=[]
        for i in range(len(candies)):
            r=candies[i]+extraCandies
            if r>=m:
                li.append(True)
            else:
                li.append(False)

        return li
            