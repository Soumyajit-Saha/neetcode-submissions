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

        def make(n, r, c):
            if n == 1:
                val = True if grid[r][c] else False
                return Node(val, True, None, None, None, None)
            mid = n // 2

            topLeft = make(mid, r, c)
            topRight = make(mid, r, c + mid)
            bottomLeft = make(mid, r + mid, c)
            bottomRight = make(mid, r + mid, c + mid)

            if (topLeft.isLeaf and topRight.isLeaf and
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return Node(topLeft.val, True)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)  

        return make(len(grid), 0, 0) 