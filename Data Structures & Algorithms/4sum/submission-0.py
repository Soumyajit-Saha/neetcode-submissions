class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        comb = []
        res = []
        nums.sort()

        def kSum(k, start, target):
            if k > 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    comb.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
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
                    res.append([nums[l], nums[r]] + comb)
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        kSum(4, 0, target)

        return res            