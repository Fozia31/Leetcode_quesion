class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = [0]* (n+1)

        for a , b in trust:
            ans[a] -= 1
            ans[b] += 1

        res = ans[1:]
        for i in range(len(res)):
            if res[i]== n - 1:
                return i + 1
        return -1