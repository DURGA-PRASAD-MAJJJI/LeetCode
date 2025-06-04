class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st=[0]
        l=[0]*len(temperatures)
        print(l)
        for i in range(1,len(temperatures)):
            while st and temperatures[i]>temperatures[st[-1]]:
                index=st.pop()
                print(index)
                l[index]=i-index
            st.append(i)
        return l