class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev_bit = n & 1
        n >>= 1
        
        while n > 0:
            curr_bit = n & 1
            if curr_bit == prev_bit:
                return False
            prev_bit = curr_bit
            n >>= 1
        
        return True
