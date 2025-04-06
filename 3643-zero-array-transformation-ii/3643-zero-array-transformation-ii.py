class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def canZero(mid):
            diff = [0] * (n + 2) 
            for i in range(mid):
                l, r, val = queries[i]
                diff[l] += val
                diff[r + 1] -= val  

            running = 0
            for i in range(n):
                running += diff[i]
                if nums[i] > running:
                    return False
            return True

        left, right = 0, len(queries)
        res = -1

        while left <= right:
            mid = (left + right) // 2
            if canZero(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res
