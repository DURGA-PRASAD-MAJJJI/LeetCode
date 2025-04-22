class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        tot=numBottles
        mt=numBottles
        while mt>=numExchange:
            new=mt // numExchange
            tot+=new
            mt=mt%numExchange+new
        return tot


        