class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        r=0
        c=0
        for i in range(len(answers)):
            if answers[i]==0:
                r+=1
            elif i==0 or answers[i]!=answers[i-1] or c==0:
                r+=answers[i]+1
                c=answers[i]
            else:
                c-=1
        return r