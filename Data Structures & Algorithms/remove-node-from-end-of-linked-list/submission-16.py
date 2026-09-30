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
        dummy = ListNode(0, head)
        remove = dummy
        while cur:
            remove = remove.next
            cur = cur.next
        remove.next = remove.next.next
        return dummy.next
        