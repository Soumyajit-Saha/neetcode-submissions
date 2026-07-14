class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = []
        perm = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
            for i in count.keys():
                if count[i] == 0:
                    continue
                count[i] -= 1
                perm.append(i)
                dfs()
                count[i] += 1
                perm.pop()

        dfs()
        return res
