class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dict_ = defaultdict(int)
        count = prefix_sum = 0
        dict_[0] = 1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            mod = prefix_sum % k
            if mod in dict_ :
                count += dict_[mod]
            dict_[mod] += 1
        return count


        