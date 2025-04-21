class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # answer = [-1]
        
        # for i in range(len(arr) - 1 , 0 , -1):
        #     cur_num = arr[i]
        #     answer.append(max(cur_num , answer[-1]))

        # return answer[::-1]
        
        max_Right = -1

        for i in range(len(arr) - 1 , -1 , -1):
            current = arr[i]
            arr[i] = max_Right
            max_Right = max(max_Right , current)
        
        return arr