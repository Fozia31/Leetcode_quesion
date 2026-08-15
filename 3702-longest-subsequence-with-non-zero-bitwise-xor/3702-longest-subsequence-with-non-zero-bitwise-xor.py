class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        totalXor = 0
        allZero = True

        for x in nums:
            totalXor ^= x
            if x > 0:
                allZero = False

        if totalXor > 0:
            return n
        return n - 1 if allZero == False else 0
        