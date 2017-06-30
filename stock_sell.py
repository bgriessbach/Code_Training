class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        max_profit=0
        cur_profit=0
        buy=prices[0]
        for item in prices:
            cur_profit=item-buy
            if cur_profit>max_profit:
                max_profit=cur_profit
            if item<buy:
                buy=item
        return max_profit
