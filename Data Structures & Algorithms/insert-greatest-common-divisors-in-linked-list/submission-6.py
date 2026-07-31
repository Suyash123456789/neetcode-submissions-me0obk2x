# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        cur = head

        while cur.next:
            n1, n2 = cur.val, cur.next.val
            val = gcd(n1, n2)
            node = ListNode(val, cur.next)
            cur.next = node
            cur = cur.next.next
        return head