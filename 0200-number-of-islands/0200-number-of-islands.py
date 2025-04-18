class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row , col):
            if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1 , col)
                dfs(row - 1  , col )
                dfs(row , col + 1)
                dfs(row , col - 1)
            else:
                return
            return 1
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row , col )
                    ans += 1

        return ans
        