class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        comb = []
        res = []
        def dfs(start):
            if len(comb) == k:
                res.append(comb.copy())
            for i in range(start, n + 1):
                comb.append(i)
                dfs(i + 1)
                comb.pop()

        dfs(1)
        return res
