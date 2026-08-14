# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.visit = False

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        if not headA or not headB:
            return None


        cur = headA
        

        while cur:
            cur.visit = True
            cur = cur.next
        cur2 = headB
       
        while cur2:
            if cur2.visit == True:
                return cur2
            cur2 = cur2.next
        return None

        