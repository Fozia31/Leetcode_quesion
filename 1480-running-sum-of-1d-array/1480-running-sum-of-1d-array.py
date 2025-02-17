class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            ans.append(sum_)
        return ans 
        