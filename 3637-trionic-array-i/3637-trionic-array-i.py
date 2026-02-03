class Solution(object):
    def isTrionic(self, nums):
        n = len(nums)
        
        if n < 4:
            return False
        
        i = 0
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        
        if i == 0 or i == n - 1:
            return False
        
        j = i
        
        while j + 1 < n and nums[j] > nums[j + 1]:
            j += 1
        
        if j == i or j == n - 1:
            return False
        
        k = j
        
        while k + 1 < n and nums[k] < nums[k + 1]:
            k += 1
        
        return k == n - 1
