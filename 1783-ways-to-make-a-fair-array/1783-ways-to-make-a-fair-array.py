class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        sum_even = sum_odd = 0
        count = 0
        left_odd = left_even = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                sum_even += nums[i]
            else:
                sum_odd += nums[i]
       
        for i in range(len(nums)):
            if i % 2 == 0:
                sum_even -= nums[i]

            else:
                sum_odd -= nums[i]

            new_even=sum_even +  left_odd
            new_odd=sum_odd + left_even

            if new_odd == new_even:
                count += 1

            if i % 2 == 0:
                left_even += nums[i]
            else:
                left_odd += nums[i] 


        return count
            
        