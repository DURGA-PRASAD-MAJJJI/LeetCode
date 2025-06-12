class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftsum=sum(cardPoints[:k])
        rightsum=0
        maxPointer=leftsum
        n=len(cardPoints)
        idx=n-1
        for i in range(k-1,-1,-1):
            leftsum-=cardPoints[i]
            rightsum+=cardPoints[idx]
            idx-=1
            maxPointer=max(maxPointer,leftsum+rightsum)
        return maxPointer