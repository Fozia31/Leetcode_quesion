class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        direction = [(1,0) , (-1 , 0),(0 ,1),(0, -1)]
        def inbound(r , c):
            if 0 <= r < rows and 0 <= c < cols:
                return True
        
        @cache
        def dfs(row , col):
            result = 1
            for dx , dy in direction:
                x = row + dx
                y = col + dy
                if inbound(x , y) and matrix[row][col] < matrix[x][y]:
                    result = max (result , 1 + dfs(x , y))

            return result
        
        height = 1
        for row in range(rows):
            for col in range(cols):
                height = max(height , dfs(row , col))

        return height
        