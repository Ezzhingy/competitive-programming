class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # o(n^2) approach
#         profit = 0
#         for i in range(len(prices)-1):
#             for j in range(i + 1, len(prices)):
#                 if prices[j] - prices[i] > profit:
#                     profit = prices[j] - prices[i]
        
#         return profit
        
        # o(n) approach
        profit = 0
        p1, p2 = 0, 1
        
        while p2 < len(prices):
            if prices[p1] < prices[p2]:
                profit = max(profit, prices[p2]-prices[p1])
            else:
                p1 = p2 
            p2 += 1
        return profit
            

                