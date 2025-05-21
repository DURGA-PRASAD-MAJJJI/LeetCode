class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = int(''.join(map(str,digits)))
        res=int(result)+1
        res2=[int(digit) for digit in str(res)]
        return res2