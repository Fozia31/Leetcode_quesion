class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        l=r=0
        sett=set()
        while r<len(s):
            while s[r] in sett:
                sett.remove(s[l])
                l +=1
            sett.add(s[r])
            r +=1
            max_length =max(max_length,r-l)
        return max_length

        