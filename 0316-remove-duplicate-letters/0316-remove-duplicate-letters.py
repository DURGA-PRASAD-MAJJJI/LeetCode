class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st=[]
        visit=set()
        print(st)
        print(visit)
        idx= {ch: i for i, ch in enumerate(s)}
        print(idx)
        for i,j in enumerate(s):
            if j in visit:
                continue
            while st and j<st[-1] and i<idx[st[-1]]:
                visit.remove(st.pop())
            st.append(j)
            visit.add(j)
        return ''.join(st)

