from collections import deque

class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = [False] * (n + 1)
        visited[1] = True
        queue = deque([1])
        ans = float("inf")

        while queue:
            node = queue.popleft()

            for nei, dist in graph[node]:
                ans = min(ans, dist)
                if not visited[nei]:
                    visited[nei] = True
                    queue.append(nei)

        return ans