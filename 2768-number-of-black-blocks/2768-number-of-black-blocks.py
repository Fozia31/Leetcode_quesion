from collections import Counter

class Solution(object):
    def countBlackBlocks(self, m, n, coordinates):
        """
        :type m: int
        :type n: int
        :type coordinates: List[List[int]]
        :rtype: List[int]
        """
        block_black_count = Counter()
        
        for r, c in coordinates:
            for dr, dc in [(0,0), (0,-1), (-1,0), (-1,-1)]:
                br = r + dr
                bc = c + dc
                if 0 <= br < m - 1 and 0 <= bc < n - 1:
                    block_black_count[(br, bc)] += 1
        
        res = [0] * 5
        for cnt in block_black_count.values():
            if 1 <= cnt <= 4:
                res[cnt] += 1
        
        total_blocks = (m - 1) * (n - 1)
        res[0] = total_blocks - sum(res[1:])
        
        return res
