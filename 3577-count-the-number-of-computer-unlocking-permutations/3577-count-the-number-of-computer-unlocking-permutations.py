class Solution(object):
    def countPermutations(self, complexity):
        """
        :type complexity: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        N = len(complexity)

        for i in range(1,N):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        for i in range(1,N):
            ans *= i

        return ans%mod

        