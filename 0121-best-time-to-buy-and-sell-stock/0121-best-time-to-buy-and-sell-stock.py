class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = None
        profit = 0

        for i in prices:
            if minBuy is None or i < minBuy:
                minBuy = i
            if i - minBuy > profit:
                profit = i - minBuy

        return profit