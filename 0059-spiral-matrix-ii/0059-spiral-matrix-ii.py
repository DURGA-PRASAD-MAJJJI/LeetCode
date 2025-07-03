class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m=[]
        for i in range(n):
            r=[]
            for j in range(n):
                r.append(0)
            m.append(r)
        a=len(m)
        b=len(m[0])
        r=(min(a,b)+1)//2
        l=[]
        c=1
        for i in range(r):
            for j in range(i,b-i):
                m[i][j]=c
                c+=1
            for j in range(i+1,a-i):
                m[j][b-i-1]=c
                c+=1
            if a-i-1!=i:
                for j in range(b-i-2,i-1,-1):
                    m[a-i-1][j]=c
                    c+=1
            if b-i-1!=i:
                for j in range(n-i-2,i,-1):
                    m[j][i]=c
                    c+=1
        return m

        