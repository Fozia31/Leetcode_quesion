class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        sett = set(nums)

        for s in sett:
            if nums.count(s) >=2:
                res.append(s)
                break
        summ = 0
        for i in range(1,len(nums)+1):
            summ += i

        res.append(summ-sum(sett))
        return res
        