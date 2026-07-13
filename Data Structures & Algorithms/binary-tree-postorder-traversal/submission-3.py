# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        res = []
        stack = []

        while stack or curr:
            if curr:
                res.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()

        return res[::-1]