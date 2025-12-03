class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        min_len = len(strs[0])
        min_index = 0
        for i in range(len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
                min_index = i
        
        candidate = strs[min_index]
        
        for i in range(min_len):
            char = candidate[i]
            for s in strs:
                if s[i] != char:
                    return candidate[:i]  
        return candidate  