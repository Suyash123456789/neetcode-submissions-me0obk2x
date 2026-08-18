# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head

        while n:
            cur = cur.next
            n -= 1
        dummy = ListNode(next = head)
        curr = dummy
        while cur:
            curr = curr.next
            cur = cur.next
        curr.next = curr.next.next
        return dummy.next
        