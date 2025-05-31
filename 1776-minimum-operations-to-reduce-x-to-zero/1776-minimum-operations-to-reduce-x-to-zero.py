class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        current_sum = 0
        number_opr = -1
        reminder = total - x
        left = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum > reminder and left <= right:
                current_sum -= nums[left]
                left += 1
            if current_sum == reminder:
                number_opr = max(number_opr , right - left + 1)
            
        if number_opr == -1:
            return -1
        return len(nums) - number_opr



