class Solution(object):
    def processStr(self, s, k):
        lengths = []
        cur = 0

        for ch in s:
            if ch == "*":
                if cur > 0:
                    cur -= 1
            elif ch == "#":
                cur *= 2
            elif ch == "%":
                pass
            else:
                cur += 1

            lengths.append(cur)

        if k >= cur:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur = lengths[i]

            if ch == "#":
                prev = cur // 2
                k %= prev

            elif ch == "%":
                k = cur - 1 - k

            elif ch == "*":
                pass

            else:
                if k == cur - 1:
                    return ch

        return '.'