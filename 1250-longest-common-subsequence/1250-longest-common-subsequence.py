class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        self.dd=[[-1 for _ in range(m+1)]for _ in range(n+1)]
        return self.solve(text1,text2,n,m)
    def solve(self,text1,text2,n,m):
        if n==0 or m==0:
            return 0
        if self.dd[n][m]!=-1:
            return self.dd[n][m]
        if text1[n-1]==text2[m-1]:
            self.dd[n][m]=1+self.solve(text1,text2,n-1,m-1)
        else:
            self.dd[n][m]=max(self.solve(text1,text2,n-1,m),self.solve(text1,text2,n,m-1))
        return self.dd[n][m]