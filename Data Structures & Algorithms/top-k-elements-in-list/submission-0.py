class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)

        revMap = {i: [] for i in range(1, len(nums) + 1)}

        for i, c in count.items():
            revMap[c].append(i)

        c = 0
        res = []
        for i in range(len(nums), 0, -1):
            for n in revMap[i]:
                res.append(n)
                c += 1
                if c == k:
                    return res

        