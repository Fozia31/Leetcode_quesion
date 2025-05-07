class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1]*len(graph)
        for i in range(len(graph)):
            if color[i] == -1:
                queue = deque([(i , 0)])

                while queue:
                    node , col = queue.popleft()
                    color[node] = col
                    
                    for nb in graph[node]:
                        if color[nb] == col:
                            return False
                        elif color[nb] == -1:
                            color[nb] = 1 - col
                            queue.append((nb ,  color[nb]))

        return True

    













    #     color = [-1]*(len(graph))

    #     for i in range(len(graph)):
    #         if color[i] == -1:
    #             queue = deque([(i , 0)])
    #             while queue:
    #                 for i in range(len(queue)):
    #                     node , col = queue.popleft()
    #                     color[node] = col
    #                     for nb in graph[node]:
    #                         if color[nb] == col:
    #                             return False
    #                         elif color[nb] == -1:
    #                             color[nb] = 1 - col
    #                             queue.append((nb ,color[nb]))


    #     return True

                        



        