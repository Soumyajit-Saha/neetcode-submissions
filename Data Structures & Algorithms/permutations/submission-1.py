class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        perm = []
        res = []

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for item in count:
                if count[item] > 0:
                    count[item] -= 1
                    perm.append(item)
                    dfs()
                    count[item] += 1
                    perm.pop()

        dfs()
        return res