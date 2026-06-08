# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        i = 0
        q = dummy
        while q:
            if i == left - 1:
                break
            q = q.next
            i += 1

        grpPrev = q

        i = 0
        q = dummy
        while i < right:
            q = q.next
            i += 1

        end = q
        grpNext = end.next

        start = grpPrev.next
        prev = grpNext
        curr = start

        while curr != grpNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        grpPrev.next = prev

        return dummy.next

        
