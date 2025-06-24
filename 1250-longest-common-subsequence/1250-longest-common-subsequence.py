class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dd=[[0 for _ in range(m+1)]for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                # if dd[i][j]!=0:
                #     return dd[i][j]
                if text1[i-1]==text2[j-1]:
                    dd[i][j]=1+dd[i-1][j-1]
                else:
                    dd[i][j]=max(dd[i-1][j],dd[i][j-1])
        return dd[n][m]