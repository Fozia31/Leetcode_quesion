class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atMost(k):
            left = 0
            odd_count = 0
            total = 0
            for right in range(len(nums)):
                if nums[right] % 2 == 1:
                    odd_count += 1
                while odd_count > k:
                    if nums[left] % 2 == 1:
                        odd_count -= 1
                    left += 1
                total += (right - left + 1)
            return total
        
        return atMost(k) - atMost(k - 1)
