class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        prev = ""
        l = 0
        r = 1
        res = 1

        while r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                prev = ">"
                r += 1
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                prev = "<"
                r += 1
            else:
                prev = ""
                if arr[r] == arr[r - 1]:
                    l = r
                    r += 1
                else:
                    # x < x < x or x > x > x
                    l = r - 1
                    r = r


        return res