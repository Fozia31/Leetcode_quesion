class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        # Try to match target from left to right
        prefix = []

        for i in range(n):
            x = ord(target[i]) - ord('a')

            if cnt[x] > 0:
                prefix.append(target[i])
                cnt[x] -= 1
            else:
                # We cannot match target[i].
                # Try the smallest character greater than target[i].
                for c in range(x + 1, 26):
                    if cnt[c] > 0:
                        prefix.append(chr(c + ord('a')))
                        cnt[c] -= 1

                        # Remaining characters in sorted order
                        for j in range(26):
                            prefix.append(chr(j + ord('a')) * cnt[j])

                        return ''.join(prefix)

                # No greater character here, so backtrack
                while prefix:
                    old = prefix.pop()
                    old_val = ord(old) - ord('a')
                    cnt[old_val] += 1

                    # Position we are replacing
                    pos = len(prefix)
                    need = ord(target[pos]) - ord('a')

                    for c in range(need + 1, 26):
                        if cnt[c] > 0:
                            prefix.append(chr(c + ord('a')))
                            cnt[c] -= 1

                            for j in range(26):
                                prefix.append(chr(j + ord('a')) * cnt[j])

                            return ''.join(prefix)

                return ""

        # s can form target exactly.
        # We need a strictly greater permutation, so backtrack.
        while prefix:
            old = prefix.pop()
            old_val = ord(old) - ord('a')
            cnt[old_val] += 1

            pos = len(prefix)
            need = ord(target[pos]) - ord('a')

            for c in range(need + 1, 26):
                if cnt[c] > 0:
                    prefix.append(chr(c + ord('a')))
                    cnt[c] -= 1

                    for j in range(26):
                        prefix.append(chr(j + ord('a')) * cnt[j])

                    return ''.join(prefix)

        return ""