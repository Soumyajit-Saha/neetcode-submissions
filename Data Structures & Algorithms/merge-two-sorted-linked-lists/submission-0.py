# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2

        head = ListNode()
        q = head

        while l1 and l2:
            if l1.val < l2.val:
                q.next = ListNode(l1.val)
                l1 = l1.next
            else:
                q.next = ListNode(l2.val)
                l2 = l2.next
            q = q.next

        while l1:
            q.next = ListNode(l1.val)
            q = q.next
            l1 = l1.next
        
        while l2:
            q.next = ListNode(l2.val)
            q = q.next
            l2 = l2.next

        return head.next
            