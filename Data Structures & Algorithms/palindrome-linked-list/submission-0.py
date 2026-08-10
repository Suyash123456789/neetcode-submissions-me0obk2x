# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        new = slow.next
        slow.next = None
        prev = None
        cur = new
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        start = prev
        cur = dummy.next
        while cur:
            if start.val != cur.val:
                return False
            start = start.next
            cur = cur.next
        return True


