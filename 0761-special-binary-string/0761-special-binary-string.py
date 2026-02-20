class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        
        specials = []
        balance = 0
        start = 0
        
        for i, ch in enumerate(s):
            balance += 1 if ch == '1' else -1
            if balance == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                specials.append("1" + inner + "0")
                start = i + 1
        
        specials.sort(reverse=True)
        return "".join(specials)