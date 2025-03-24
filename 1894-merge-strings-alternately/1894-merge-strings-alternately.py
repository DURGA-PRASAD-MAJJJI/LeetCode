class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        li=[]
        for i in range(len(word1)):
            li.append(word1[i])
            for j in range(len(word2)):
                li.append(word2[j])
                word2=word2[1:]
                break
        if(len(word2)!=0):
            li.append(word2)
        return "".join(li)
        
                
        