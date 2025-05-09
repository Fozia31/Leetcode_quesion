class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        arr = []
        n = len(edges)
        parent = [i for i in range(1 ,( n + 1))]
        size = [1]*n

        def find(x):
            if x != parent[x - 1]:
                parent[x - 1] = find(parent[x - 1])
            
            return parent[x - 1]

        def union(x , y):
            E_x = find(x)
            E_y = find(y)
            if E_x != E_y:
                if size[E_y - 1] > size[E_x - 1]:
                    size[E_y - 1] += size[E_x - 1]
                    parent[E_x -1] = E_y
                else:
                    size[E_x -1] += size[E_y - 1]  
                    parent[E_y - 1] = E_x

        for v1 , v2 in edges:

            if find(v1) == find(v2):
                arr.append([v1, v2])
                
            else:
                union(v1 , v2)

        return arr[-1]
                
             


        