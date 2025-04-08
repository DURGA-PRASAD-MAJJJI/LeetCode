class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mini = float('inf')
        li=[]
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    r=i+j
                    print(r)
                    if r<mini:
                        mini=r
                        li = [list2[j]]
                    elif r==mini:
                        li.append(list2[j])    
        return li