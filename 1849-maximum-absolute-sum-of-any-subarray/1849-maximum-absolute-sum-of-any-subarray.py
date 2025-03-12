class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        cur_sum = 0
        max_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            max_sum = max(max_sum , cur_sum)

            if cur_sum < 0:
                cur_sum = 0

        cur_sum = 0
        min_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            min_sum = min(min_sum , cur_sum)

            if cur_sum > 0:
                cur_sum = 0
                
        if abs(min_sum) > abs(max_sum):
            return abs(min_sum)
        else:
            return abs(max_sum)