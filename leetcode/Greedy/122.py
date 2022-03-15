class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        hold = prices[0]

        for price in prices:
            if hold < price:
                result += price - hold

            hold = price

        return result
