class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if (prices[i] - min)>profit:
                profit = prices[i] - min
            if prices[i]<min:
                min=prices[i]
        return profit

        
        