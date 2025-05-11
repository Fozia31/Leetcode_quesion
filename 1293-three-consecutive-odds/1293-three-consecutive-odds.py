class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left , middle , right = 0 , 1, 2

        while right < len(arr):
            if (arr[left]%2 !=0) and (arr[middle]%2 !=0) and( arr[right]%2 !=0):
                return True

            left += 1
            middle += 1
            right += 1
        return False

        