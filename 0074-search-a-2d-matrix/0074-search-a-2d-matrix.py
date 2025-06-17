class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n,m=len(matrix),len(matrix[0])
        s,e=0,(n*m)-1
        while(s<=e):
            mid=(s+e)//2
            row_idx=mid//m
            col_idx=mid%m
            temp=matrix[row_idx][col_idx]
            if temp==target:
                return True
            elif temp<target:
                s=mid+1
            else:
                e=mid-1
        return False