class Solution(object):
    def maxStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positives = []
        negatives = []
        zeros = 0
        
        for x in nums:
            if x > 0:
                positives.append(x)
            elif x < 0:
                negatives.append(x)
            else:
                zeros += 1

        negatives.sort()

        if len(negatives) % 2 != 0:
            negatives.pop()

        if not positives and not negatives:
            return 0 if zeros > 0 else max(nums)

        result = 1
        for x in positives:
            result *= x
        for x in negatives:
            result *= x

        return result
