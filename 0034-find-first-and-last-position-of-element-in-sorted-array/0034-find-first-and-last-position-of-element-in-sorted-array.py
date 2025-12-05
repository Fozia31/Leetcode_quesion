class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target not in nums:
            return [-1,-1]
        else:
            start = bisect.bisect_left(nums,target)
            end = bisect.bisect_right(nums,target)
            return [start,end-1]

        