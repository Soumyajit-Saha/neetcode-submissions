class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comb = []
        res = []
        candidates.sort()
        
        
        def dfs(start, curr):
            if curr > target:
                return
            if curr == target:
                res.append(comb.copy())
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                dfs(i + 1, curr + candidates[i])
                comb.pop()
        
        dfs(0, 0)
        return res
            
