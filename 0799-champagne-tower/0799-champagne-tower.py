class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0.0] * 101 for _ in range(101)]
        dp[0][0] = float(poured)

        for r in range(query_row + 1):
            for c in range(r + 1):
                if dp[r][c] > 1.0:
                    overflow = (dp[r][c] - 1.0) / 2.0
                    dp[r][c] = 1.0
                    dp[r + 1][c] += overflow
                    dp[r + 1][c + 1] += overflow

        return dp[query_row][query_glass]
