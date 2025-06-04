class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[0]
        n=len(temperatures)
        l=[0]*n
        for i in range(1,n):
            while st and temperatures[i]>temperatures[st[-1]]:
                p=st.pop()
                l[p]=i-p
            st.append(i)
        return l