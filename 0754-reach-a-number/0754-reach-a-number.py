class Solution(object):
    def reachNumber(self, target):
        target = abs(target)
        s = 0
        k = 0
        while True:
            k += 1
            s += k
            if s >= target and (s - target) % 2 == 0:
                return k
