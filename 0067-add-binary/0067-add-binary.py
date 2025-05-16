class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_binary = bin(int(a, 2) + int(b, 2))
        return sum_binary[2:]