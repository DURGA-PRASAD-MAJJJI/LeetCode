class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            elif len(st)==0:
                return False
            else:
                k=st.pop()
                if i==")":
                    if k!='(':
                        return False
                elif i=="}":
                    if k!="{":
                        return False
                elif i=="]":
                    if k!="[":
                        return False   
        
        if len(st)==0:
            return True
        else:
            return False                    
                          
        