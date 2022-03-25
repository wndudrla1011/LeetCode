class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        earnings = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(min_price, price)
            earnings = max(earnings, price - min_price)

        return earnings