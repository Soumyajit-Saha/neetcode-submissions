class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # The idea is to see what can be the minimum of largest sum in a partition
        # It will be max(nums) as in all possible partitionings, that item can be left alone and it will be the max of sum of all parts
        # Maximum of largest sum will be sum of all nums
        # Perform binary search on this range, and check if we can get <= k partitions with each partition sum <= mid of binary search, keep on checking for the minimum possible value between max(nums) and sum(nums)

        l = max(nums)
        r = sum(nums)
        res = 0

        def canSplit(largest):
            currSum = 0
            subarrayCount = 0
            for num in nums:
                currSum += num
                if currSum > largest:
                    subarrayCount += 1
                    # as num made the curr sum go beyond largest, re-initialize currSum to num
                    currSum = num
            return subarrayCount + 1 <= k

        while l <= r:
            mid = l + (r - l) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res