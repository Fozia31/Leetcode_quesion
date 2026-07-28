from collections import Counter

class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)

        left = []
        middle = ""

        for ch in sorted(count.keys()):
            left.append(ch * (count[ch] // 2))
            if count[ch] % 2 == 1:
                middle = ch

        left = "".join(left)
        return left + middle + left[::-1]