# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_kth(node):
            i = 0
            while node and i < k:
                node = node.next
                i += 1
            return node

        dummy = ListNode(next=head)

        grpPrev = dummy
        start = head

        while True:
            end = get_kth(grpPrev)
            if not end:
                break
            grpNext = end.next

            prev = grpNext
            curr = start

            while curr != grpNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            grpPrev.next = prev
            grpPrev = start
            start = grpNext

        return dummy.next
