class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        ans = [-1] * n  
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            ans[i] = stack[-1] if stack else -1
            stack.append(i)
            next = [n] * n      
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next[i] = stack[-1] if stack else n
            stack.append(i)
            total_sum = 0
        for i in range(n):
            left_count = i - ans[i]   
            right_count = next[i] - i  
            total_sum = (total_sum + arr[i] * left_count * right_count) % MOD
        
        return total_sum



            