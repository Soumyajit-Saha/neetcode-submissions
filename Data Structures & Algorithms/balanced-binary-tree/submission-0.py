# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0
            leftBalanced, left = dfs(node.left)
            rightBalanced, right = dfs(node.right)

            if not leftBalanced or not rightBalanced:
                return False, 0
            if abs(left - right) <= 1:
                return True, 1 + max(left, right)
            else:
                return False, 0

        balanced, _ = dfs(root)
        return balanced