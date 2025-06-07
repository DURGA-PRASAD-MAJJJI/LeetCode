from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        l=list(digits)
        di={
            '1': None,
            '2':"abc",
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        l1=[]
        for i in range(len(l)):
            print(l[i])
            if l[i] in di:
                r=di.get(l[i])
                l1.append(r)
        if len(l1)<=0:
            return []
        return [''.join(i) for i in product(*l1)]

        
        