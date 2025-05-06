class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(mat) , len(mat[0])
        queue = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row , col))
                    visited.add((row , col))
        
        ans = 1
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def inbound(r , c):
            if 0 <= r < rows and 0 <= c< cols:
                return True
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for d_r , d_c in directions:
                    d_r = d_r + r
                    d_c = d_c + c
                    if (d_r , d_c) not in visited and inbound(d_r , d_c):
                        queue.append((d_r , d_c))
                        visited.add((d_r , d_c))     
                        mat[d_r][d_c] = ans
            ans +=1

        return mat   