class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Suffix minimum
        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = min(nums[i], suffix[i + 1])

        # Prefix maximum
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix[i] <= k:
                return i

        return -1