class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        comb = []
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(comb.copy())
                return
            comb.append(nums[i])
            dfs(i + 1)
            comb.pop()
            dfs(i + 1)

        dfs(0)
        return res