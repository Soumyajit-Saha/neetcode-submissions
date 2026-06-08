# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def getKthNode(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode()

        dummy.next = head

        groupPrev = dummy

        while True:
            # groupPrev -> 1 -> 2 -> 3 -> groupNext 
            start = groupPrev.next
            kth = getKthNode(start, k - 1)

            if not kth: # kth node from start is None, leave it
                break

            groupNext = kth.next

            curr = start
            prev = groupNext

            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            groupPrev.next = kth
            groupPrev = start
            
        return dummy.next
