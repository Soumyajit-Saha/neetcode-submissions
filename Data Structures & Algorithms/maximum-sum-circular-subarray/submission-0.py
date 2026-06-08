class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        localMax = nums[0]
        globalMax = nums[0]
        localMin = nums[0]
        globalMin = nums[0]

        total = nums[0]

        for num in nums[1:]:
            total += num
            localMax = max(num, num + localMax)
            globalMax = max(localMax, globalMax)
            localMin = min(num, num + localMin)
            globalMin = min(localMin, globalMin)

        if globalMax < 0: # all negatives
            return globalMax
        else:
            return max(globalMax, total - globalMin)