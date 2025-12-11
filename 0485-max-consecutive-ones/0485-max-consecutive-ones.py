class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                continue
            else:
                res = max(res , r-l)
                l=r+1
        res = max(res, len(nums) - l)
        return res