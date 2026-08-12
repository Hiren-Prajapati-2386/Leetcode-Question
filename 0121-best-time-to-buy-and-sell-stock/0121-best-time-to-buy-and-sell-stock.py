class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        low = 0

        for i in range(1,len(prices)):

            if prices[low] > prices[i]:
                low = i

            profit = max(profit,prices[i] - prices[low])

        return profit
        