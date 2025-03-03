class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        k = 3
        lag = 0
        
        for i in range(len(nums) - k + 1):
            a = []
            a = nums[i:k]
            k += 1
            print(a)
            if a[0] + a[1] > a[2]:
                lag = max(lag , a[0] + a[1] + a[2])
                print(lag)

        return lag
            
        