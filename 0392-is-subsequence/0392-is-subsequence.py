class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    c += 1
                    t = t[j+1:]
                    break
        if len(s) == c:
            return True
        else:
            return False
