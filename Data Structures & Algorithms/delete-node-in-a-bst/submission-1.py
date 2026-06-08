# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
            return root
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
            return root
        else:
            # If the node has one or no child
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # If node has both children
            curr = root.right
            # Find inorder successor
            while curr.left:
                curr = curr.left

            succ = curr
            # replace value of root with succ and delete succ
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

            return root

