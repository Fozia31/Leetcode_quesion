class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows ,cols =  len(isWater) ,len(isWater[0])
        queue = deque()
        visited = set()
        water_cell = []

        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    queue.append((row,col))
                    visited.add((row , col))
                    water_cell.append((row , col))
        ans = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def inbound (r , c):
            if 0 <= x < rows and 0 <= y < cols:
                return True

        while queue:
            for i in range(len(queue)):
                r , c = queue.popleft()
                for x, y in directions:
                    x = x + r
                    y = y + c
                    if (x,y) not in visited and inbound(x , y):
                        queue.append((x,y))
                        visited.add((x,y))
                        isWater[x][y] = ans
            ans += 1

        for row , col in water_cell :
            isWater[row][col] = 0

        return isWater
        
        