class Solution(object):
    def maxSumTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        NEG = float('-inf')

        up1 = NEG
        down = NEG
        up2 = NEG
        ans = NEG

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            curr = nums[i]

            if prev < curr:
                up1 = max(up1, prev) + curr
                up2 = max(up2, down) + curr
                ans = max(ans, up2)
                down = NEG

            elif prev > curr:
                down = max(down, up1) + curr
                up1 = NEG
                up2 = NEG

            else:
                up1 = NEG
                down = NEG
                up2 = NEG

        return ans
