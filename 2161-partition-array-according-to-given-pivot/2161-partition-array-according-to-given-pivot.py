class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less_than_pivot = []
        great_than_pivot = []
        equal_pivot = []

        for num in nums:
            if num < pivot:
                less_than_pivot.append(num)
            elif num > pivot:
                great_than_pivot.append(num)
            else:
                equal_pivot.append(num)

        return less_than_pivot + equal_pivot + great_than_pivot
        