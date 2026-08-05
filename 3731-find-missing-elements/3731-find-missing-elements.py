class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_ = min(nums)
        max_ = max(nums)
        ans = []

        for i in range(min_,max_+1):
            if i not in nums:
                ans.append(i)
        return ans