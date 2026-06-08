class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        comb = []
        res = []

        def dfs(i, onGoingSum):
            if onGoingSum > target:
                return
            if onGoingSum == target:
                res.append(comb.copy())
                return

            for i in range(i, len(nums)):
                comb.append(nums[i])
                dfs(i, onGoingSum + nums[i])
                comb.pop()
            
        dfs(0, 0)
        return res