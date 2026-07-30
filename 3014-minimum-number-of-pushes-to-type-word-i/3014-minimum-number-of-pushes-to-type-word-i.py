class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        N = len(word) 

        remain = N % 8
        whole = N // 8

        return remain * (whole + 1) + 8 * sum(range(whole + 1))
        