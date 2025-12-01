class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = 0
        for pos in position:
            if pos % 2 != 0:
                odd += 1
        even = len(position) - odd
        return min(odd, even)
