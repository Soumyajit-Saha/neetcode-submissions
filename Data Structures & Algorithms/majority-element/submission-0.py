class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 0
        for i in nums[1:]:
            if i == majority:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 0
                    majority = i

        return majority
