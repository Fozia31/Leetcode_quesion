class Solution:
    def generate(self , n):
        if n == 1:
            return "0"
        st = self.generate(n - 1)
        return  st + "1" + "".join("1" if bit == "0" else "0" for bit in st[::-1])

    def findKthBit(self, n: int, k: int) -> str:
        return self.generate(n)[k - 1]
        