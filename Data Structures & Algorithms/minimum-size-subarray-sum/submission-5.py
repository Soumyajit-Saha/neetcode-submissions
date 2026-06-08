class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = float('inf')
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            if currSum >= target:
                res = min(res, r - l + 1)

                while currSum >= target:
                    res = min(res, r - l + 1)
                    currSum -= nums[l]
                    l += 1

        return res if res != float('inf') else 0
