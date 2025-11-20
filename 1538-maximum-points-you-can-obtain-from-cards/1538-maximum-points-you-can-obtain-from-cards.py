class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        l=sum(cardPoints[:k])
        r=0
        maxx=l
        for i in range(1,k+1):
            l-=cardPoints[k-i]
            r+=cardPoints[n-i]
            maxx=max(maxx,l+r)
        return maxx