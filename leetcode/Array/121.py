class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min, result = prices[0], 0

        for i, price in enumerate(prices):
            if left_min > price:
                left_min = price
            else:
                result = max(result, price - left_min)

        return max(result, 0)
