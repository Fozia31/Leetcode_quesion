class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        MOD = 10**9 + 7

        h = [1] + sorted(hFences) + [m]
        v = [1] + sorted(vFences) + [n]

        hs = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                hs.add(h[j] - h[i])

        mx = 0
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                d = v[j] - v[i]
                if d in hs:
                    mx = max(mx, d)

        if mx == 0:
            return -1
        return (mx * mx) % MOD
