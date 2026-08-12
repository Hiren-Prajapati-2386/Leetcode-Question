class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        drink = numBottles
        empty = numBottles
        
        while(empty >= numExchange):
            newBottles = empty // numExchange
            empty = empty % numExchange

            drink += newBottles
            empty += newBottles

        
        return drink 
        