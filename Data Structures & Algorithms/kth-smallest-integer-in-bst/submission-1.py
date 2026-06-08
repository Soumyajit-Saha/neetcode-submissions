# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = root.val
        c = k
        def dfs(node):
            nonlocal res, c
            if not node:
                return
            dfs(node.left)
            c -= 1
            if c == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res