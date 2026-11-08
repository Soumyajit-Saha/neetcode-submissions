class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)

        res = 1
        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                l = 0
                curr = nums[i]
                while curr in nums_set:
                    l += 1
                    curr += 1

                res = max(res, l)

        return res
