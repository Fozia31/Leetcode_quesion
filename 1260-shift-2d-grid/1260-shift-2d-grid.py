class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        row = len(grid)
        column = len(grid[0])

        for _ in range(k):
            last = grid[row - 1][column - 1]  # Save the last element

            # Traverse backwards
            for i in range(row - 1, -1, -1):
                for j in range(column - 1, -1, -1):
                    if i == 0 and j == 0:
                        grid[0][0] = last
                    elif j == 0:
                        grid[i][0] = grid[i - 1][column - 1]
                    else:
                        grid[i][j] = grid[i][j - 1]

        return grid