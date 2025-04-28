class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        graph = [[[],[]] for _ in range(n)]
        for a, b in redEdges:
            graph[a][0].append(b)
        for a , b in blueEdges:
            graph[a][1].append(b)

        queue = deque([(0, 0), (0 , 1)])
        visited = set([(0, 0), (0 , 1)])
        dist = 0
        answer = [-1]*n
        while queue:
            for i in range(len(queue)):
                node , color = queue.popleft()
                if answer[node] == -1:
                    answer[node] = dist
                next_color = 1 - color
                for nb in graph[node][next_color]:
                    if (nb , next_color) not in visited:
                        visited.add((nb , next_color))
                        queue.append((nb , next_color))
                        

            dist += 1
        return answer
        