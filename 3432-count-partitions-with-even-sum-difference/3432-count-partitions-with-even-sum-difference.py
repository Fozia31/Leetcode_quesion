class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(1,len(nums)):
            left = nums[:i+1]
            right = nums[i+1:]
            cur_sum = sum(left) -sum(right)
            if abs(cur_sum)%2 == 0:
                count += 1

        return count
