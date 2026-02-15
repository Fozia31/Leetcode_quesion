class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            total = digit_a + digit_b + carry
            carry = total // 2
            result.append(str(total % 2))
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])
