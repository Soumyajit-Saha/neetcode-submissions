class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return True
            # left and mid values are same, keep increasing left as we cannot make any decision
            if nums[l] == nums[mid]:
                l += 1
            # Left and mid is in left portion
            elif nums[l] < nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right and mid in Right portion
            else:
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return False