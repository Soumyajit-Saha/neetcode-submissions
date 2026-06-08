# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: idx for idx, val in enumerate(inorder)}

        def dfs(preo, ino):
            if not preo or not ino:
                return None
            node = TreeNode(preo[0])
            mid = ino.index(preo[0])
            node.left = dfs(preo[1: mid + 1], ino[: mid])
            node.right = dfs(preo[mid + 1: ], ino[mid + 1: ])
            return node

        return dfs(preorder, inorder)