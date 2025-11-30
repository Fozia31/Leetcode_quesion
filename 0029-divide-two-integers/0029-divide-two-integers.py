class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        a, b = abs(dividend), abs(divisor)
        ans = 0

        while a >= b:
            shift = 0
            while (b << (shift + 1)) <= a:
                shift += 1
            a -= b << shift
            ans += 1 << shift

        return sign * ans
