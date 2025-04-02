class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        counter = Counter(nums)
        ans = []

        for key , value in counter.items():
            if value == 2:
                ans.append(key)

        return ans 
       
    