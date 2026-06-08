class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in s:
                l = 0
                next_num = nums[i]
                while next_num in s:
                    l += 1
                    next_num += 1
                res = max(res, l)
            
        return res
