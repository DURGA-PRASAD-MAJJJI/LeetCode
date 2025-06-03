class Solution:
    def clumsy(self, n: int) -> int:
        if n == 0:
            return 0
        st=[n]
        n-=1
        i=0
        while n>0:
            if i%4==0:
                st[-1]*=n
            elif i%4==1:
                st[-1] = int(st[-1] / n) 
            elif i%4==2:
                st.append(n)
            else:
                st.append(-n)
            n-=1
            i+=1
        return sum(st)
        
