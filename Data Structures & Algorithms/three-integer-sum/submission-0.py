class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        comb = []
        res = []
        nums.sort()
        def ksum(start, target, k):
            if k > 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i - 1] == nums[i]:
                        continue
                    comb.append(nums[i])
                    ksum(i + 1, target - nums[i], k - 1)
                    comb.pop()
                return
            
            l = start
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append(comb + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        ksum(0, 0, 3)
        return res