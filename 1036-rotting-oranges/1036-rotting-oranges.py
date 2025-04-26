class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        visited = set()
        time = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row , col))
                    visited.add((row , col))
                    
        def inbound(nrow , ncol):
            if 0 <= nrow < rows and 0 <= ncol < cols :
                return True
            else:
                return False

        dirction = [(0, 1), (0 , -1), (1 , 0) ,(-1 ,0)]
        newRow , newCol = 0 , 0
        while queue:
            Rotten = False
            for _ in range(len(queue)):
                r , c = queue.popleft()
                for dr ,dc in dirction:
                    newRow = dr + r
                    newCol = dc + c
                    if inbound(newRow , newCol) and grid[newRow][newCol] ==1:
                        grid[newRow][newCol] = 2
                        visited.add((newRow , newCol))
                        queue.append((newRow , newCol))
                        Rotten = True
            if Rotten:
                time += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1 

        return time




        