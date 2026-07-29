class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""

        for i in range(26):
            half[i] = freq[i] // 2
            if freq[i] % 2:
                mid = chr(ord('a') + i)

        if self.countPermutations(half, k) < k:
            return ""

        left = []
        m = len(s) // 2

        for _ in range(m):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                cnt = self.countPermutations(half, k)

                if k > cnt:
                    k -= cnt
                    half[c] += 1
                else:
                    left.append(chr(ord('a') + c))
                    break

        left = "".join(left)
        return left + mid + left[::-1]

    def countPermutations(self, freq, cap):
        ans = 1
        total = 0

        for f in freq:
            if f == 0:
                continue

            if total == 0:
                total += f
                continue

            n = total + f
            limit = min(f, total)

            for i in range(1, limit + 1):
                ans = ans * (n - i + 1) // i
                if ans > cap:
                    return cap + 1

            total += f

        return ans