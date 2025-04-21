class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if nums == sorted(nums):
            return True
        else:
            count = 0
            left , right = 0 , 1
            while right < len(nums):
                if nums[left] > nums[right]:
                    count += 1
                    if count > 1:
                            return False
                    if left > 0 and nums[left - 1] > nums[right]:
                        nums[right] = nums[left]
                    else:
                        nums[left] = nums[right]
                        
                left += 1
                right += 1

        return True
                                 

        