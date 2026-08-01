class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        memo = {}
        
        def helper(i, j):
            if i == j:
                return nums[i]
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = max(nums[i] - helper(i + 1, j), nums[j] - helper(i, j - 1))
            return memo[(i, j)]
        
        return helper(0, len(nums) - 1) >= 0
