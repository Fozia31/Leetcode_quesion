class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = s.count('1')
        ans = total

        segments = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((s[i], j - i))
            i = j

        for i in range(1, len(segments) - 1):
            if (segments[i][0] == '1' and
                segments[i - 1][0] == '0' and
                segments[i + 1][0] == '0'):

                gain = segments[i - 1][1] + segments[i + 1][1]
                ans = max(ans, total + gain)

        return ans