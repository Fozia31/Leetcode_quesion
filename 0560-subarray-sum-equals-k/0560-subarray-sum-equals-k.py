class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        dict_[0] = 1
        count = prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            rem_ = prefix_sum - k

            count += dict_[rem_]

            dict_[prefix_sum] += 1
        return count
