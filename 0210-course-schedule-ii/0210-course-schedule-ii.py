class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        queue = deque()
        order = []

        for courses , pre in prerequisites:
            graph[pre].append(courses)
            indegree[courses] += 1
        print(indegree)

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neig in graph[node]:
                indegree[neig] -=1
                if indegree[neig] == 0:
                    queue.append(neig)
            order.append(node)
        
        if len(order) > numCourses or len(order) < numCourses:
            return []
        return order


        