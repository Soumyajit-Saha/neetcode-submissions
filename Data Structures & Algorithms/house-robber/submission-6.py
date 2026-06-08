class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        first = 0
        second = 0
        res = max(first, second)

        for i in range(len(nums)):
            res = max(second, first + nums[i])
            first = second
            second = res

        return res