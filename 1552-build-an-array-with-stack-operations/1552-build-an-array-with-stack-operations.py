from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        li = []
        for i in range(1, n + 1):
            stack.append(i)
            if i in target:
                li.append("Push")
            else:
                stack.pop()
                li.append("Push")
                li.append("Pop")
            if len(stack) == len(target):
                break
        # print(li)
        return li
