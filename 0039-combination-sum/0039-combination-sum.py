class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = [] 
        
        def backtrack(start, comb, remain):
            if remain == 0:
                res.append(list(comb))
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    continue  
                comb.append(candidates[i])
                backtrack(i, comb, remain - candidates[i])  
                comb.pop()  

        backtrack(0, [], target)
        return res
