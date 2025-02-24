class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0]*n
        suffix_sum = [0]*n
        sum_ = 0
        result = [0]*n

        for i in range(n): 
            prefix_sum[i] = sum_
            sum_ += nums[i]
        sum_ = 0

        for i in range(n-1,-1,-1):
            suffix_sum[i] = sum_
            sum_ += nums[i]
        
        for i in range(n):
            result[i]=((i*nums[i])-prefix_sum[i]) + (suffix_sum[i]- (nums[i] * (n-i-1)))
            
        return result
