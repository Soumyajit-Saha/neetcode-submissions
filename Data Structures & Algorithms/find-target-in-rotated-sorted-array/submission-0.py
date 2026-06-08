class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot():
            l = 0
            r = len(nums) - 1
            res = nums[l]
            pivot = l

            while l <= r:
                if nums[l] <= nums[r]:
                    if nums[l] < res:
                        res = nums[l]
                        pivot = l

                        break

                mid = l + (r - l) // 2
                if res > nums[mid]:
                    res = nums[mid]
                    pivot = mid

                if nums[l] <= nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return pivot

        pivot = findPivot()
        l = 0
        r = len(nums) - 1

        if nums[pivot] <= target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1


        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1