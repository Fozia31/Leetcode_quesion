class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res = []
        first_half = nums[:n]
        second_half = nums[n:]

        for i in range(len(first_half)):
            res.append(first_half[i])
            res.append(second_half[i])

        return res

