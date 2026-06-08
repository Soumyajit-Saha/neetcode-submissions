class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        local_max = nums[0]
        local_min = nums[0]
        global_max = nums[0]

        for i in range(1, len(nums)):
            temp = local_max
            local_max = max(local_max * nums[i], nums[i], local_min * nums[i])
            local_min = min(temp * nums[i], nums[i], local_min * nums[i])
            global_max = max(local_max, global_max)

        return global_max