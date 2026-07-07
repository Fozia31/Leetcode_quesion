class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        non_zero = ""
        digit_sum = 0

        for ch in str(n):
            digit_sum += int(ch)
            if ch != "0":
                non_zero += ch

        if non_zero == "":
            return 0

        return int(non_zero) * digit_sum