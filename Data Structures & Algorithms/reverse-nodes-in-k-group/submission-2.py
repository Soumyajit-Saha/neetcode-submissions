# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(node):
            count = 0
            while node:
                if count == k:
                    break
                node = node.next
                count += 1
            return node

        dummy = ListNode()
        dummy.next = head

        grpPrev = dummy

        while True:
            kth = getKth(grpPrev)

            if not kth:
                break

            grpNext = kth.next
            start = grpPrev.next

            prev = grpNext

            curr = start

            while curr != grpNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            grpPrev.next = prev
            grpPrev = start

        
        return dummy.next

