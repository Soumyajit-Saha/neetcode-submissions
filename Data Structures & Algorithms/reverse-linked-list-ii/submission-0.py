# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        i = 1
        q = dummy
        while i < left:
            q = q.next
            i += 1

        start = q

        i = 0
        q = dummy
        while i < right:
            q = q.next
            i += 1

        end = q.next

        prev = end
        curr = start.next

        while curr != end:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        start.next = prev

        return dummy.next

        
