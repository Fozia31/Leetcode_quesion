class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dic_ = defaultdict(int)
        stack = []
        ans = []
        for i in range(len(temperatures)):
                while stack and    temperatures[i] > stack[-1][0]:
                    dic_[stack[-1][1] ] = i - stack[-1][1] 
                    stack.pop()
                stack.append([temperatures[i] , i])
        
        return [dic_[i] for i in range((len(temperatures)))]
        