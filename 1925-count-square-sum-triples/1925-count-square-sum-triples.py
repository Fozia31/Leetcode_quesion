class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    continue
                else:
                    cur_sqrt = sqrt((i*i) + (j*j))
                    if cur_sqrt.is_integer():
                        if cur_sqrt <= n:
                            count +=1

        return count
