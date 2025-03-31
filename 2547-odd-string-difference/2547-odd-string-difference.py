from typing import List
class Solution:
    def oddString(self, word_list: List[str]) -> str:
        get_diff = lambda word: [ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word))]
        word_list.sort(key=get_diff)
        return word_list[0] if get_diff(word_list[0]) != get_diff(word_list[1]) else word_list[-1]
