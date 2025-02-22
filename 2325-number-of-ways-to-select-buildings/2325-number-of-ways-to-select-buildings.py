class Solution:
    def numberOfWays(self, s: str) -> int:
        suf_0, suf_1 = s.count('0'), s.count('1')
        pre_0, pre_1 = 0, 0 
        
        total = 0
        
        for j in range(len(s)):
            if s[j] == '0':
                total += pre_1 * suf_1 
                pre_0 += 1
                suf_0 -= 1
            else: 
                total += pre_0 * suf_0  
                pre_1 += 1
                suf_1 -= 1
                
        return total
