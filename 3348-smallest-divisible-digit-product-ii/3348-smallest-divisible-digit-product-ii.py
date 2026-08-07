DIGIT_FACTORS = {
    1: (0,0,0,0), 2: (1,0,0,0), 3: (0,1,0,0), 4: (2,0,0,0),
    5: (0,0,1,0), 6: (1,1,0,0), 7: (0,0,0,1), 8: (3,0,0,0), 9: (0,2,0,0),
}

_min_ab_cache = {}

def _min_ab(a, b):
    key = (a, b)
    cached = _min_ab_cache.get(key)
    if cached is not None:
        return cached
    best = None
    for x6 in range(0, b + 1):
        x8 = -(-max(0, a - x6) // 3)
        x9 = -(-max(0, b - x6) // 2)
        cost = x6 + x8 + x9
        if best is None or cost < best:
            best = cost
    _min_ab_cache[key] = best
    return best

def _sub(need, have):
    return tuple(max(0, n - h) for n, h in zip(need, have))

def _minimal_len(req):
    a, b, c, d = req
    return _min_ab(a, b) + c + d

def _construct(req, r):
    res = []
    cur = req
    for pos in range(r):
        remaining_after = r - pos - 1
        for dgt in range(1, 10):
            new_req = _sub(cur, DIGIT_FACTORS[dgt])
            if _minimal_len(new_req) <= remaining_after:
                res.append(str(dgt))
                cur = new_req
                break
    return "".join(res)


class Solution(object):
    def smallestNumber(self, num, t):
        """
        :type num: str
        :type t: int
        :rtype: str
        """
        rem = t
        a = b = c = d = 0
        for p in (2, 3, 5, 7):
            while rem % p == 0:
                rem //= p
                if p == 2: a += 1
                elif p == 3: b += 1
                elif p == 5: c += 1
                else: d += 1
        if rem != 1:
            return "-1"
        need = (a, b, c, d)

        n = len(num)
        L = _minimal_len(need)
        if L > n:
            return _construct(need, L)

        digits = [int(ch) for ch in num]
        prefix = [(0,0,0,0)] * (n + 1)
        for i in range(n):
            f = DIGIT_FACTORS.get(digits[i], (0,0,0,0))
            prefix[i+1] = tuple(x + y for x, y in zip(prefix[i], f))

        first_zero = n
        for i, dg in enumerate(digits):
            if dg == 0:
                first_zero = i
                break

        if first_zero == n:
            if _sub(need, prefix[n]) == (0,0,0,0):
                return num

        limit = min(first_zero, n - 1)
        for i in range(limit, -1, -1):
            base = prefix[i]
            remaining_len = n - 1 - i
            for dgt in range(digits[i] + 1, 10):
                new_base = tuple(x + y for x, y in zip(base, DIGIT_FACTORS[dgt]))
                leftover = _sub(need, new_base)
                if _minimal_len(leftover) <= remaining_len:
                    return num[:i] + str(dgt) + _construct(leftover, remaining_len)

        return _construct(need, n + 1)