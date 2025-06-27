class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=str(x)
        i=0
        j=len(l)-1
        while(i<=j):
            if l[i]==l[j]:
                i+=1
                j-=1
            else:
                break
        if i>j:
            return True
        else:
            return False
        