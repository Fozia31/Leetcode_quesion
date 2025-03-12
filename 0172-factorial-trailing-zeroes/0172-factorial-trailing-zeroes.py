class Solution:
    
    def fact(self, n , k):
        if n // k < 1:
            return 0
        return  (n // k) + self.fact(n , k*5)

    def trailingZeroes(self, n: int) -> int:

        return self.fact(n , 5)

    
        