class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums=sum(nums)
        sum_n=0
        for i in range(len(nums)+1):
            sum_n +=i
        return sum_n - sum_nums           
        