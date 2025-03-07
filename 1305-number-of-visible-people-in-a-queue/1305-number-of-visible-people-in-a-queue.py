class Solution:
    def canSeePersonsCount(self, heights):
        stack = []
        ans = [0] * len(heights) 
        
        for i in range(len(heights) - 1, -1, -1):
            pop_count = 0
            
            while stack and heights[i] > stack[-1]:
                stack.pop()
                pop_count += 1
            if stack:
                ans[i] = pop_count + 1
            else:
                ans[i] = pop_count
            
            stack.append(heights[i])
        
        return ans
