class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        row_index = -1
        
        for i in range(len(mat)):
            count_ones = mat[i].count(1)
            
            if count_ones > max_ones:
                max_ones = count_ones
                row_index = i
        
        return [row_index, max_ones]
