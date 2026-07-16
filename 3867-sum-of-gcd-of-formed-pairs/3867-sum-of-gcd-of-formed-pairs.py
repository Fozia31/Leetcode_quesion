from fractions import gcd

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix_gcd = [0] * n
        mx = 0

        for i in range(n):
            mx = max(mx, nums[i])
            prefix_gcd[i] = gcd(nums[i], mx)

        prefix_gcd.sort()

        ans = 0
        for i in range(n // 2):
            ans += gcd(prefix_gcd[i], prefix_gcd[n - 1 - i])

        return ans