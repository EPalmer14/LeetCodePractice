class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = -1
        sell = -1
        
        for x in range(1, len(prices)):
            if(prices[x] > prices[x - 1] and buy == -1):
                buy = prices[x - 1]
            if(prices[x] < prices[x - 1] and sell == -1 and buy != -1):
                sell = prices[x - 1]
            if(buy != -1 and sell != -1):
                profit += sell - buy
                buy = -1
                sell = -1
        
        if(buy != -1):
            sell = prices[-1]
        profit += sell - buy
        
        return profit
                
            
            