# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        ans = 0
        low = 0 
        high = n
        while low <= high:
            mid = (low+high) // 2
            if isBadVersion(mid) == False :
                low = mid + 1
            elif isBadVersion(mid) == True :
                ans = mid
                high = mid - 1

        return ans
        