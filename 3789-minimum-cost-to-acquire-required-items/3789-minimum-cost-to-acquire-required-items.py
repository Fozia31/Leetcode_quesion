class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        option1 = need1 * cost1 + need2 * cost2

        both1 = min(need1, need2)
        option2 = both1 * costBoth + (need1 - both1) * cost1 + (need2 - both1) * cost2

        both2 = max(need1, need2)
        option3 = both2 * costBoth

        return min(option1, option2, option3)