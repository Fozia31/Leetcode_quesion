class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        map_s_t = {}
        map_t_s = {}

        for ch1, ch2 in zip(s, t):
            if ch1 not in map_s_t and ch2 not in map_t_s:
                map_s_t[ch1] = ch2
                map_t_s[ch2] = ch1
            else:
                if map_s_t.get(ch1) != ch2 or map_t_s.get(ch2) != ch1:
                    return False

        return True
