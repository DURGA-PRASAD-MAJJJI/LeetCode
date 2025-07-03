class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n=len(matrix)
        m=len(matrix[0])
        l=[]
        r = (min(n,m)+1)//2
        for i in range(r):
            for j in range(i,m-i):
                l.append(matrix[i][j])
            for j in range(i+1,n-i):
                l.append(matrix[j][m-i-1])
            if n-i-1!=i:
                for j in range(m-i-2,i-1,-1):
                    l.append(matrix[n-i-1][j])
            if m-i-1!=i:
                for j in range(n-i-2,i,-1):
                    l.append(matrix[j][i])
        return l
