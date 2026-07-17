# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        indMap = {inorder[i]: i for i in range(len(inorder))}
        n = len(postorder) - 1

        self.i = 0
        def dfs(l, r):
            if l > r:
                return None
            val = postorder[n - self.i]
            ind = indMap[val]
            node = TreeNode(val)
            self.i += 1
            node.right = dfs(ind + 1, r)
            node.left = dfs(l, ind - 1)
            return node

        return dfs(0, len(inorder) - 1)