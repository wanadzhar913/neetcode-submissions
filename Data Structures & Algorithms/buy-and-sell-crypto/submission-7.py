class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(0, len(prices) - 1):
            buy_price = min(buy_price, prices[i])
            profit = max(profit, prices[i+1] - buy_price)

        return profit
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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

        # Used hint 
        # min_price = prices[0]
        # max_profit = 0
        # n = len(prices)

        # for i in range(n):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     if prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price

        # return max_profit

        # Optimal
        # lowest_price = prices[0]
        # profit = 0
        # for p in prices:
        #     lowest_price = min(lowest_price, p)
        #     profit = max(profit, p - lowest_price)
        
        # return profit

        # Using Two Pointers
        