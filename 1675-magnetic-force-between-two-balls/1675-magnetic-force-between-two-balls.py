class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def Ischeck(mid):

            count = 1
            cur_pos = position[0]

            for num in position[1:]:
                if (num -  cur_pos) >= mid:
                    count += 1
                    cur_pos = num
            
            return count >= m

        position.sort()
        result = 0
        low = 1
        high = position[-1] - position[0]

        while low <= high:
            mid = (low + high) // 2

            if Ischeck(mid):
                result = mid 
                low = mid + 1
            else:
                high = mid - 1

        return result




        
        