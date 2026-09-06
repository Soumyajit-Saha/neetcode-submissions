class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []

        def dfs(start, combSum):
            if combSum == target:
                res.append(comb[:])
                return

            if combSum > target:
                return

            for i in range(start, len(nums)):
                comb.append(nums[i])
                dfs(i, combSum + nums[i])
                comb.pop()
            
        dfs(0, 0)
        return res