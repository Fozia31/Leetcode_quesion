class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        indegree = [0]*len(graph)
        queue = deque()
        safe_node = []
        adj_node = [[] for _ in range(len(graph))]

        for i in range(len(graph)):
            curr = graph[i]
            indegree[i] = len(curr)
            if indegree[i] == 0:
                queue.append(i)
            for node in curr:
                adj_node[node].append(i)

        while queue:
            node = queue.popleft()
            for neig in adj_node[node]:
                indegree[neig] -=1
                if indegree[neig] == 0:
                    queue.append(neig)
            safe_node.append(node)

        return sorted(safe_node)
        