# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merge(l1, l2):
            head = ListNode()
            q = head

            while l1 and l2:
                if l1.val < l2.val:
                    node = ListNode(l1.val)
                    q.next = node
                    l1 = l1.next
                else:
                    node = ListNode(l2.val)
                    q.next = node
                    l2 = l2.next
                q = q.next

            while l1:
                node = ListNode(l1.val)
                q.next = node
                l1 = l1.next
                q = q.next

            while l2:
                node = ListNode(l2.val)
                q.next = node
                l2 = l2.next
                q = q.next

            return head.next
            

        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList = merge(l1, l2)
                temp.append(mergedList)

            lists = temp

        return lists[0]