class Solution:
    def balancedStringSplit(self, s: str) -> int:

        ans = 0
        balancer = 0
        for j in s:
            if j == "R":
                balancer -= 1
            elif j == "L":
                balancer += 1

            if balancer == 0:
                ans += 1
            
        return ans


        