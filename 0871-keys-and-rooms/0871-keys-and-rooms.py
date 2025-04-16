class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = set([0])
        queue = deque([0])
        while queue:
            
            curr_key = queue.popleft()

            for key in rooms[curr_key]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        

        return len(visited) == len(rooms)



