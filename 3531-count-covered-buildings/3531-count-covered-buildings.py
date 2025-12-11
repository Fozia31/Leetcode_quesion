class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """

        from collections import defaultdict

        rows = defaultdict(list)   
        cols = defaultdict(list)   

        for r, c in buildings:
            rows[r].append(c)
            cols[c].append(r)

        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        count = 0
        for r, c in buildings:
            has_left_and_right = (rows[r][0] < c < rows[r][-1])
            has_up_and_down = (cols[c][0] < r < cols[c][-1])

            if has_left_and_right and has_up_and_down:
                count += 1

        return count
