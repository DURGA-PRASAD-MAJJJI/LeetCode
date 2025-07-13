class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
                players.sort()
                trainers.sort()
                a,b=len(players),len(trainers)
                i=j=count=0
                while i<a and j<b:
                    while j< b and players[i]>trainers[j]:
                        j+=1
                    if j<b:
                        count+=1
                    i+=1
                    j+=1

                return count