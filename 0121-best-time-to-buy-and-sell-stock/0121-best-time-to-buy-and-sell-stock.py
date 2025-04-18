class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        answer = 0
        left , right = 0 , 0

        while right < len(prices):
            
            if prices[right] < prices[left]:
                left = right
                
            answer = max(answer , prices[right] - prices[left])
            right += 1

        return answer


