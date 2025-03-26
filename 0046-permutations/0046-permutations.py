class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack( combination):
            if len(combination) == len(nums):
                ans.append(combination[:])
                return

            for i in range(len(nums)):
                if nums[i] in combination:
                    continue

                combination.append(nums[i])
                backtrack(combination)
                combination.pop()
        
        backtrack([])
        return ans


        