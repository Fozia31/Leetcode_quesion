class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_ = 0
        a = []
        for i , j in enumerate(nums):
            a.append((j , i))
        a.sort()
        for i , j in a:
            while stack and j < stack[-1]:
                stack.pop()
            stack.append(j)
            max_ = max(max_ , stack[-1] - stack[0])


        return max_ 
        