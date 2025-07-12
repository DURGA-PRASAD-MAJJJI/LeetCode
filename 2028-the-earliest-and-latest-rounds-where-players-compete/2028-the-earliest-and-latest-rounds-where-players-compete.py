class Solution:
    def earliestAndLatest(self, totalPlayers: int, playerA: int, playerB: int) -> list[int]:
        def simulateRounds(numPlayers, posA, posB):
            if posA + posB == numPlayers + 1:
                return (1, 1)
            if posA > posB:
                posA, posB = posB, posA
            if numPlayers <= 4:
                return (2, 2)
            half = (numPlayers + 1) // 2
            earliestRound, latestRound = float('inf'), float('-inf')
            if posA - 1 > numPlayers - posB:
                temp = numPlayers + 1 - posA
                posA = numPlayers + 1 - posB
                posB = temp
            if posB * 2 <= numPlayers + 1:
                leftGroup = posA - 1
                middleGroup = posB - posA - 1
                for i in range(leftGroup + 1):
                    for j in range(middleGroup + 1):
                        minRound, maxRound = simulateRounds(half, i + 1, i + j + 2)
                        earliestRound = min(earliestRound, minRound + 1)
                        latestRound = max(latestRound, maxRound + 1)
            else:
                mirroredPosB = numPlayers + 1 - posB
                leftGroup = posA - 1
                middleGroup = mirroredPosB - posA - 1
                rightGroup = posB - mirroredPosB - 1
                for i in range(leftGroup + 1):
                    for j in range(middleGroup + 1):
                        newPosB = i + j + 1 + (rightGroup + 1) // 2 + 1
                        minRound, maxRound = simulateRounds(half, i + 1, newPosB)
                        earliestRound = min(earliestRound, minRound + 1)
                        latestRound = max(latestRound, maxRound + 1)
            return (earliestRound, latestRound)
        return list(simulateRounds(totalPlayers, playerA, playerB))
