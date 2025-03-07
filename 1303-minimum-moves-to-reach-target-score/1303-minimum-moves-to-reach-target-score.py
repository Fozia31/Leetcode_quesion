class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:

        min_move = 0
        while target > 1:

            if target % 2 == 0 and maxDoubles > 0:
                target //= 2
                maxDoubles -= 1
                min_move += 1

            elif maxDoubles == 0:
               min_move +=  target - 1
               break
               
            else:
                target -= 1
                min_move += 1

        return min_move
                


        