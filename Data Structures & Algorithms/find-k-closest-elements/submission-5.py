class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # First find the index equal to or just less that x
        # If no element smaller than x, index is 0
        l = 0
        r = len(arr) - 1
        index = 0
        res = []

        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                index = mid
                break
            if arr[mid] < x:
                index = mid
                l = mid + 1
            else:
                r = mid - 1

        # Check neighbours of index
        # If left is closer decrement left
        # If right is close increment right
        left = index
        right = index + 1

        res = []

        while left >= 0 and right < len(arr):
            if abs(arr[left] - x) < abs(arr[right] - x):
                res = [arr[left]] + res
                left -= 1
            elif abs(arr[left] - x) > abs(arr[right] - x):
                res.append(arr[right])
                right += 1
            else:
                res = [arr[left]] + res
                left -= 1
            if len(res) == k:
                return res
        
        while left >= 0:
            res = [arr[left]] + res
            left -= 1
            if len(res) == k:
                return res

        while right < len(arr):
            res.append(arr[right])
            right += 1
            if len(res) == k:
                return res
