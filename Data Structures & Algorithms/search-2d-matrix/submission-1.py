class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search which row it belongs to

        l = 0
        r = len(matrix) - 1

        foundRow = -1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                foundRow = mid
                break
            
            if target < matrix[mid][0]:
                r -= 1
            
            else:
                l += 1

        if foundRow == -1:
            return False


        # search in that row

        l = 0
        r = len(matrix[0]) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[foundRow][mid] == target:
                return True
            
            if target < matrix[foundRow][mid]:
                r -= 1
            
            else:
                l += 1

        return False