class Solution(object):
    def maxProfit(self, prices, strategy, k):
        n = len(prices)
        base_profit = 0
        for i in range(n):
            base_profit += strategy[i] * prices[i]

        s_prof = [0] * (n + 1)
        s_price = [0] * (n + 1)

        for i in range(n):
            s_prof[i + 1] = s_prof[i] + strategy[i] * prices[i]
            s_price[i + 1] = s_price[i] + prices[i]

        best_gain = 0
        half = k // 2

        for start in range(n - k + 1):
            end = start + k
            new_window_profit = s_price[end] - s_price[start + half]
            base_window_profit = s_prof[end] - s_prof[start]
            gain = new_window_profit - base_window_profit
            if gain > best_gain:
                best_gain = gain

        return base_profit + best_gain
