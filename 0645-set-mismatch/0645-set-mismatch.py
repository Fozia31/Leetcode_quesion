class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()

        start = 0
        end = len(nums)
        while start < end:
            if nums[start] == nums[start + 1]:
                missing = sum(range(1, len(nums) + 1)) - sum(set(nums))

                return [nums[start] , missing]
            start += 1
            



        