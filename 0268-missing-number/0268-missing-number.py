class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        range_xor = 0
        arr_xor = 0

        for i in range(len(nums) + 1):
            range_xor ^=i

        for num in nums:
            arr_xor ^= num
        return arr_xor ^ range_xor
        