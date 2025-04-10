class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        rows = len(board)
        cols = len(board[0])
        def dfs(row , col):
            if 0 <= row < rows and 0 <= col < cols and board[row][col] == "O":
                board[row][col] = "S"

                dfs(row + 1 , col)
                dfs(row - 1 , col)
                dfs(row  , col + 1)
                dfs(row  , col - 1)
            else:
                return

        for row in range(rows):
            if board[row][0] == "O":
                dfs(row , 0)
            if board[row][cols - 1]:
                dfs(row , cols - 1)
        
        for col in range(cols):
            if board[0][col] == "O":
                dfs(0 , col)
            if board[rows - 1][col]:
                dfs(rows - 1 , col)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return board
        
