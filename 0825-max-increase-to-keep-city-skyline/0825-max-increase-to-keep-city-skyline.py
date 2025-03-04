class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        n = len(grid)

        max_row = [max (grid[i]) for i in range(n)]
        max_col = []
        for i in range(n):
            max_ = 0
            for j in range(n):
                max_ = max(max_ , grid[j][i])
            max_col.append(max_)
            
        count = 0
        for i in range(n):
            for j in range(n):
                y = abs(grid[i][j] - min(max_row[i] , max_col[j]))
                count += y
            
        return count        