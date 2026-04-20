class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0
        profit = []
        for i in range(n):
            for j in range(i + 1, n):
                profit.append(prices[j] - prices[i])
        if max(profit) <= 0:
            return 0
        return max(profit)

        