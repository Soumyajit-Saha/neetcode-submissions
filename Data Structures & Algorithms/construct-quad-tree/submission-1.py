"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def make(row_start, row_end, col_start, col_end):
            if row_start > row_end or col_start > col_end:
                return None
            if row_start == row_end and col_start == col_end:
                val = True if grid[row_start][col_start] else False
                return Node(val, True, None, None, None, None)
            row_half = (row_end + row_start) // 2
            col_half = (col_end + col_start) // 2
            topLeft = make(row_start, row_half, col_start, col_half)
            topRight = make(row_start, row_half, col_half + 1, col_end)
            bottomLeft = make(row_half + 1, row_end, col_start, col_half)
            bottomRight = make(row_half + 1, row_end, col_half + 1, col_end)

            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)  

        return make(0, len(grid) - 1, 0, len(grid[0]) - 1) 