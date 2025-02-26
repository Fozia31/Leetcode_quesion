class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
            max_len = 0
            sum_ = 0
            dict_ = {0: -1}  
            for i in range(len(nums)):
                sum_ += 1 if nums[i] == 1 else -1  
                if sum_ in dict_:
                    max_len = max(max_len, i - dict_[sum_])
                else:
                    dict_[sum_] = i  
            return max_len

                