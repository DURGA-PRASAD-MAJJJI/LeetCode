class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        mini,maxx,curr=0,0,0
        for d in differences:
            curr+=d
            mini=min(mini,curr)
            maxx=max(maxx,curr)
        mini_str=lower-mini
        maxx_str=upper-maxx
        return max(0, maxx_str - mini_str + 1)


        