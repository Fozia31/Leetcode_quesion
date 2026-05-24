class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        
        n = len(arr)
        dp = [0] * n

        def dfs(i):
            if dp[i]:
                return dp[i]

            best = 1

            # check left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            # check right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                best = max(best, 1 + dfs(j))

            dp[i] = best
            return best

        ans = 1

        for i in range(n):
            ans = max(ans, dfs(i))

        return ans