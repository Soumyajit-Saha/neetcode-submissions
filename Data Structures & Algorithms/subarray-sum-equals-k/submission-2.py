class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}

        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr - k in prefix:
                res += prefix[curr - k]
            prefix[curr] = 1 + prefix.get(curr, 0)

        return res