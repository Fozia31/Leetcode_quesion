class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if arr[i] == 0:
                return True

            if i in visited:
                continue

            visited.add(i)

            forward = i + arr[i]
            backward = i - arr[i]

            if forward < len(arr):
                stack.append(forward)

            if backward >= 0:
                stack.append(backward)

        return False