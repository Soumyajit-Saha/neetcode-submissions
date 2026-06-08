class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        first = nums[0]
        second = max(nums[0], nums[1])
        res1 = max(first, second)

        for i in range(2, len(nums) - 1):
            res1 = max(second, nums[i] + first)
            first = second
            second = res1

        first = nums[1]
        second = max(nums[1], nums[2])
        res2 = max(first, second)

        for i in range(3, len(nums)):
            res2 = max(second, nums[i] + first)
            first = second
            second = res2

        return max(res1, res2)

        
