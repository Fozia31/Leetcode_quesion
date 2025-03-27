class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            if nums[i] < ans:
                ans = nums[i]
        return ans
            
        