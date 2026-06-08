class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = []
        sub = [0]

        def dfs(i):
            if i == len(nums):
                res.append(sub[0])
                return
            prevSub = sub[0]
            sub[0] = sub[0] ^ nums[i]
            dfs(i + 1)
            sub[0] = prevSub
            dfs(i + 1)

        dfs(0)
        return sum(res)
