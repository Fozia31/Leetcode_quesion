from bisect import bisect_right

class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        n = len(nums)
        max_keep = 0

        for i in range(n):
            j = bisect_right(nums, nums[i] * k)
            max_keep = max(max_keep, j - i)

        return n - max_keep
