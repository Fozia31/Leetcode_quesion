class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sett = []
        
        def backtrack(i , com):

            sett.append(com[:])

            for j in range(i , len(nums)):
                com.append(nums[j])
                backtrack(j + 1 , com)
                com.pop()
            
        backtrack( 0 , [])
        return sett
        