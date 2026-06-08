class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        count = Counter(nums)

        def dfs():
            if len(nums) == len(perm):
                res.append(perm.copy())
            for i in count:
                if count[i] > 0:
                    perm.append(i)
                    count[i] -= 1
                    dfs()
                    perm.pop()
                    count[i] += 1
        dfs()

        return res