class Solution:
    def lengthOfLongestSubstring(self, s):
        exits=set()
        for i in s:
            if i in exits:
                return False
            return exits.add(i)
        return True
    s=input()
    if