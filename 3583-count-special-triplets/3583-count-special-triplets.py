class Solution(object):
    def specialTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        right = Counter(nums)
        left = Counter()
        ans = 0

        for x in nums:
            right[x] -= 1

            two_x = x * 2

            ans = (ans + left.get(two_x, 0) * right.get(two_x, 0)) % MOD

            left[x] += 1

        return ans
