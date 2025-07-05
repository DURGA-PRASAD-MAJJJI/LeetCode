class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        for i in mat:
            i.insert(0, -1)
            i.append(-1)
        m = len(mat[0])
        mat.insert(0, [-1] * m)
        mat.append([-1] * m)
        n = len(mat)
        l = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                l[j][i] = mat[i][j]
        # for row in l:
        #     print(row)
        for i in range(1,n-1):
            # print(mat[i])
            r=mat[i]
            r1=mat[i-1]
            r2=mat[i+1]
            for j in range(1,m-1):
                # print('->>',r[j])
                if r1[j]<r[j] and r2[j]<r[j] and r[j-1]<r[j] and r[j+1]<r[j]:

                    return [i-1,j-1]
