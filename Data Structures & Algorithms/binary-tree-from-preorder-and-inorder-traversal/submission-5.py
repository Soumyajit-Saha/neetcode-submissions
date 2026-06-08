# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        for i, val in enumerate(inorder):
            indexMap[val] = i

        self.count = 0
        def dfs(l, r):
            if l > r:
                return None
            val = preorder[self.count]
            mid = indexMap[val]
            self.count += 1
            node = TreeNode(val)
            node.left = dfs(l, mid - 1)
            node.right = dfs(mid + 1, r)
            return node

        return dfs(0, len(inorder) - 1)