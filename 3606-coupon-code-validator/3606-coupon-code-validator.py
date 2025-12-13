class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        
        businessReq = set([ "electronics", "grocery", "pharmacy", "restaurant"])
        good_coupon = []

        def good(code):
            if len(code) == 0:
                return False
            for c in code:
                if c.isalpha() or c.isnumeric() or c == "_":
                    continue
                return False
            return True

        for c,b,a in zip(code,businessLine,isActive):
            if not a:
                continue
            if b not in businessReq:
                continue
            if not good(c):
                continue
            good_coupon.append([b,c])

        good_coupon.sort()
        return [c for _,c in good_coupon]

            
