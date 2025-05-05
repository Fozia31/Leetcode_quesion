class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        left , right = 0, 1
        while right < len(heights):
            if heights[right] > heights[left]:
                heapq.heappush(heap ,heights[right] - heights[left] )

            if len(heap) > ladders:
                smallest = heapq.heappop(heap)
                bricks -= smallest
                if bricks < 0:
                    return right - 1
                
            right +=1
            left  +=1
            
        return right - 1


                