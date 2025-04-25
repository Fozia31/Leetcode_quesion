class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        graph = [set() for _ in range(numCourses)]
        for pre , course in prerequisites:
            graph[pre].add(course)

        for i in range(numCourses):
            for j in range(numCourses):
                if i in graph[j]:
                    graph[j].update(graph[i])

        answer = []
        for u , v in queries :
            if v in graph[u]:
                answer.append(True)
            else:
                answer.append(False)

        return answer


        