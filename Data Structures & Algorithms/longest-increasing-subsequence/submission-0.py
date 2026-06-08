import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # keep the incresing numbers in dp.
        # if a smaller number than top of dp is found, insert the new number in the dp in the sorted position
        dp = []
        dp.append(nums[0])
        res = 1

        for i in range(1, len(nums)):
            print(dp)
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                res += 1
            else:
                ind = bisect.bisect_left(dp, nums[i])
                dp[ind] = nums[i]

        return res
