class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # find peak
        peak = 0
        l = 0
        size = mountainArr.length()
        r = size - 1

        while l <= r:
            mid = l + (r - l) // 2
            left, m, right = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if left < m > right:
                peak = mid
                break
            elif left > m > right:
                r = mid - 1
            else:
                l = mid + 1

        # find in left
        l = 0
        r = peak

        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1

        # find in right
        l = peak + 1
        r = size - 1

        while l <= r:
            mid = l + (r - l) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1

        return -1
