"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}
        def dfs(node):
            if not node:
                return None
            if node.val in nodeMap:
                return nodeMap[node.val]
            newNode = Node(node.val)
            nodeMap[node.val] = newNode

            for nei in node.neighbors:
                newNei = dfs(nei)
                newNode.neighbors.append(newNei)
            return newNode

        return dfs(node)
