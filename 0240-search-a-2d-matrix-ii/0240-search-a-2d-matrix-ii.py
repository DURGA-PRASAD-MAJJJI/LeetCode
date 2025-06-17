class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        for i in matrix:
            l,h=0,len(i)-1
            while l<=h:
                mid=(l+h)//2
                if i[mid]==target:
                    return True
                elif i[mid]<target:
                    l=mid+1
                else:
                    h=mid-1
        return False
        