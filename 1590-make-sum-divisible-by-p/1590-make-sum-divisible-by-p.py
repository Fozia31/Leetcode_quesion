class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        total = sum(nums)
        r = total % p
        if r == 0:
            return 0
        
        last_index = {0: -1}
        prefix = 0
        ans = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - r + p) % p
            if target in last_index:
                ans = min(ans, i - last_index[target])
            last_index[prefix] = i
        
        return ans if ans < len(nums) else -1
