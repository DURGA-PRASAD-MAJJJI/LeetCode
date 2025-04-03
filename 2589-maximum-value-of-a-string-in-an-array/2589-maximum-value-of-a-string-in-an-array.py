class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        c=0
        for i in strs:
            if i.isdigit():
                c=max(c,int(i))
            else:
                c=max(c,len(i))

        return c