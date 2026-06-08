import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = []

        for i in range(len(nums)):
            if not LIS:
                LIS.append(nums[i])
            else:
                if nums[i] > LIS[-1]:
                    LIS.append(nums[i])
                else:
                    ind = bisect.bisect_left(LIS, nums[i])
                    LIS[ind] = nums[i]
        
        return len(LIS)