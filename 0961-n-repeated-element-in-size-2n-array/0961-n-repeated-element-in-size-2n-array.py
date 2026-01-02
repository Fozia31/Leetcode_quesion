class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        N = len(nums)

        for n in nums:
            if nums.count(n) >= N//2:
                return n
            