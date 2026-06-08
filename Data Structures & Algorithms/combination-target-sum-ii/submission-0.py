class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        comb = []

        def dfs(index, onGoingSum):
            if onGoingSum > target:
                return
            if onGoingSum == target:
                res.append(comb.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                dfs(i + 1, onGoingSum + candidates[i])
                comb.pop()
            
        dfs(0, 0)
        return res