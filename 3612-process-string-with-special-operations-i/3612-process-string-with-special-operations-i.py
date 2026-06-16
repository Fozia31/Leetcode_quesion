class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for st in s:
            if st == "*":
                result = result[:-1]
            elif st == "#":
                result = result + result
            elif st == "%":
                result = result[::-1]
            else:
                result += st

        return result
        
        