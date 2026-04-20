class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n = len(prices)
        # if n == 1:
        #     return 0
        # profit = []
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         profit.append(prices[j] - prices[i])
        # if max(profit) <= 0:
        #     return 0
        # return max(profit)

        min_price = prices[0]
        max_profit = 0
        n = len(prices)

        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price

        return max_profit



        