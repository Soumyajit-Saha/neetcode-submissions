# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        left = head
        right = head.next

        while right:
            d = gcd(left.val, right.val)
            left.next = ListNode(d, right)
            left = right
            right = right.next

        return head

