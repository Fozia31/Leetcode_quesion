class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """

        indegree = [0]*n
        adj = defaultdict(list)
        ans = []
        for a,b in invocations:
            adj[a].append(b)
            indegree[b] += 1

        susp = set()
        def dfs(node):
            susp.add(node)

            for nei in adj[node]:
                if nei not in susp:
                    dfs(nei)
        dfs(k)

        for a, b in invocations:
            if a not in susp and b in susp:
                for i in range(n):
                    ans.append(i)
                return ans 
        for i in range(n):
            if i not in susp:
                ans.append(i)
        return ans