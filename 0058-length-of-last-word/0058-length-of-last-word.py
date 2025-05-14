class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res=s.split()
        result=len(res[-1])
        return result