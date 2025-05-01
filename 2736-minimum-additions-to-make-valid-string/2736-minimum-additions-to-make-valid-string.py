class Solution:
    def addMinimum(self, word: str) -> int:
        p,pr=0,'z'
        for i in word:
            p+=i<=pr
            pr=i
        return p*3-len(word)
        