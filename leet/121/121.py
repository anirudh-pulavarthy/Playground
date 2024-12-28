class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                # identify the profit
                current_profit = prices[r] - prices[l]
                max_profit = max(current_profit, max_profit)
                r += 1

            else:
                # don't buy on l, buy on r
                # update l to r & increment r by 1
                l, r = r, r + 1

        return max_profit