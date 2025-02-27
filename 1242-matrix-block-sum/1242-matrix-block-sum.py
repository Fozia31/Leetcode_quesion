class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        p_sum = [[0] * len(mat[0]) for j in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                p_sum[i][j] += mat[i][j]
                if i > 0:
                    p_sum[i][j] += p_sum[i-1][j]
                if j > 0:
                    p_sum[i][j] += p_sum[i][j-1]
                if i > 0 and j > 0:
                    p_sum[i][j] -= p_sum[i-1][j-1]
        
        ans = [[0] * len(mat[0]) for j in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                r_start = i - k
                if r_start < 0:
                    r_start = 0
                c_start = j - k
                if c_start < 0:
                    c_start = 0
                r_stop = i + k
                if r_stop >= len(mat):
                    r_stop = len(mat)-1
                c_stop = j + k
                if c_stop >= len(mat[i]):
                    c_stop = len(mat[i])-1

                ans[i][j] += p_sum[r_stop][c_stop]
                if r_start > 0 and c_start > 0:
                    ans[i][j] += p_sum[r_start - 1][c_start - 1]
                if c_start > 0:
                    ans[i][j] -= p_sum[r_stop][c_start - 1]
                if r_start > 0:
                    ans[i][j] -= p_sum[r_start - 1][c_stop]


        return ans
        