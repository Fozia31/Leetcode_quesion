class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        graph = defaultdict(list)

        for key , value in edges:
            graph[value].append(key)

        answer = [set() for _ in range(n)]

        def dfs(parent , key):
            
            for member in parent:
                if member not in answer[key] :
                    answer[key].add(member)
                    dfs(graph[member] , key)


        for key in range(n):
            dfs(graph[key] , key)

        return [sorted(list(a)) for a in answer]

        