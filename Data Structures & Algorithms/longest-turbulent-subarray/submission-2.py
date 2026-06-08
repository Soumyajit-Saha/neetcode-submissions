class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        greater = 0
        l = 0
        r = 1
        res = 1

        while r < len(arr):
            if greater == 0:
                if arr[r] < arr[r - 1]:
                    greater = -1
                    res = max(res, r - l + 1)
                    r += 1
                elif arr[r] > arr[r - 1]:
                    greater = 1
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    l = r
                    r += 1
                    greater = 0
            elif greater == 1:
                if arr[r] > arr[r - 1]:
                    greater = 0
                    l = r - 1
                    r = r
                elif arr[r] == arr[r - 1]:
                    greater = 0
                    l = r
                    r += 1
                else:
                    greater = -1
                    res = max(res, r - l + 1)
                    r += 1
            else:
                if arr[r] < arr[r - 1]:
                    greater = 0
                    l = r - 1
                    r = r
                elif arr[r] == arr[r - 1]:
                    greater = 0
                    l = r
                    r += 1
                else:
                    greater = 1
                    res = max(res, r - l + 1)
                    r += 1

        return res