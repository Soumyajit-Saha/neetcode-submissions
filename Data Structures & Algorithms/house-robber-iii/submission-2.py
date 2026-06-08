# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {}

        def dfs(node):
            if not node:
                return 0
            if node in dp:
                return dp[node]
            res = node.val
            if node.left:
                res += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                res += dfs(node.right.left) + dfs(node.right.right)
            res = max(res, dfs(node.left) + dfs(node.right))
            dp[node] = res
            return dp[node]

        return dfs(root)