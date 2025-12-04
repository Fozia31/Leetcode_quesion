class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        n = len(directions)
        l = 0
        
        while l < n and directions[l] == 'L':
            l += 1
        
        r = n - 1
        
        while r >= 0 and directions[r] == 'R':
            r -= 1
        
        collisions = 0
        
        for i in range(l, r + 1):
            if directions[i] != 'S':
                collisions += 1
        
        return collisions
