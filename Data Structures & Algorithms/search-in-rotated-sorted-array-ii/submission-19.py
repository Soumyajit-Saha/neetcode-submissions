class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return True
            elif nums[l] == nums[mid]:
                l += 1
            elif nums[l] < nums[mid]:
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False