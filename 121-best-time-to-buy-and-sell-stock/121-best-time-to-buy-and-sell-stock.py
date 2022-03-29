class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = sys.maxsize
        profit = 0

        for i, price in enumerate(prices):
            if minPrice > price:
                minPrice = price

            if 0 < i < len(prices):
                if prices[i] - minPrice > profit:
                    profit = prices[i] - minPrice
                    
        return profit