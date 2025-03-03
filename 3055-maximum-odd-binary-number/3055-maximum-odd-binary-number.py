class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        count_one , count_zero = 0 , 0

        for i in s:
            if i == "0":
                count_zero += 1
            else:
                count_one += 1

        ans = ""
        remider_one = count_one - 1
        
        ans += "1" * (remider_one) + "0" * count_zero + "1" *(count_one - remider_one)

        return ans 
        