class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        dic={}
        l=[]
        for i in nums2:
            while st and i>st[-1]:
                dic[st.pop()]=i
            st.append(i)
        for j in nums1:
            l.append(dic.get(j, -1))
        return l
        