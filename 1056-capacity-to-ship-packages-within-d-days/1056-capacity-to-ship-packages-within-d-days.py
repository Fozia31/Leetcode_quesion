class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def isValid(capacity):
            sum_weights = 0
            day_counter = 1
            for n in weights:
                if sum_weights + n <= mid:
                    sum_weights += n
                else:
                    day_counter += 1
                    sum_weights = n

            return day_counter <= days

        low = max(weights)
        high = sum(weights)
        ans = high

        while low <= high :
            mid = (low+high)  // 2

            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans


        
