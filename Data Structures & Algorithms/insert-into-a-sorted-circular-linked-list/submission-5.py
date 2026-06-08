# Definition for a Node.
# class Node:
#   def __init__(self, val=None, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node


        q = head
        while q.next != head:
            if q.val <= insertVal <= q.next.val:
                node = Node(insertVal)
                temp = q.next
                q.next = node
                node.next = temp
                return head
            if q.val > q.next.val and (q.val <= insertVal or insertVal <= q.next.val):
                node = Node(insertVal)
                temp = q.next
                q.next = node
                node.next = temp
                return head

            q = q.next

        node = Node(insertVal)
        temp = q.next
        q.next = node
        node.next = temp
        return head
        
