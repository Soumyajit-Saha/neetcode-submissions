class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            res = max(second, first + nums[i])
            first = second
            second = res

        return res