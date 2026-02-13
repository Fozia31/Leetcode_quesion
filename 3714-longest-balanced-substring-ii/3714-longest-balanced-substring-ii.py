class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        max_len = 0

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            max_len = max(max_len, j - i)
            i = j

        for char1, char2 in [('a', 'b'), ('b', 'c'), ('a', 'c')]:
            segments = s.split(list({'a', 'b', 'c'} - {char1, char2})[0])
            for seg in segments:
                if not seg: continue
                diff_map = {0: -1}
                diff = 0
                for idx, char in enumerate(seg):
                    diff += 1 if char == char1 else -1
                    if diff in diff_map:
                        max_len = max(max_len, idx - diff_map[diff])
                    else:
                        diff_map[diff] = idx

        three_map = {(0, 0): -1}
        ca, cb, cc = 0, 0, 0
        for i, char in enumerate(s):
            if char == 'a': ca += 1
            elif char == 'b': cb += 1
            else: cc += 1
            
            key = (ca - cb, cb - cc)
            if key in three_map:
                max_len = max(max_len, i - three_map[key])
            else:
                three_map[key] = i
                
        return max_len