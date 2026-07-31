# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head

        grpPrev = dummy

        def getKth(node):
            count = 0
            while count < k and node:
                node = node.next
                count += 1
            return node

        while True:
            start = grpPrev.next

            curr = grpPrev
            kth = getKth(curr)

            if not kth:
                break

            grpNext = kth.next

            prev = grpNext
            curr = start

            while curr != grpNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            grpPrev.next = prev
            grpPrev = start
        
        return dummy.next

