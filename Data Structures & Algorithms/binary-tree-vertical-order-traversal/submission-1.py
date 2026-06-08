# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        colMap = defaultdict(list)

        q = deque()

        q.append((0, root))

        while q:
            for _ in range(len(q)):
                col, node = q.popleft()
                colMap[col].append(node.val)
                if node.left:
                    q.append((col - 1, node.left))
                if node.right:
                    q.append((col + 1, node.right))
        
        res = []
        for k in sorted(colMap.keys()):
            res.append(colMap[k])

        return res