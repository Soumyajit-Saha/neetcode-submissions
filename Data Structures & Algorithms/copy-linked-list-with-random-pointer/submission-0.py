"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        nodeMap = {}

        head2 = Node(0)
        q1 = head
        q2 = head2

        while q1:
            node = Node(q1.val, q1.next, q1.random)
            q2.next = node
            nodeMap[q1] = node
            q1 = q1.next
            q2 = q2.next

        q = head2.next

        while q:
            q.random = nodeMap[q.random] if q.random else None
            q = q.next

        return head2.next

        