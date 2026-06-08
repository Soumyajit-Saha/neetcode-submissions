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

        # Until length of left to right is k + 1, to leave room for 1 outside k
        while right - left + 1 <= k + 1:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

        return arr[left + 1: right]
