# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        

        while len(lists) > 1:
            mergeList = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2  = lists[i + 1] if (i + 1) < len(lists) else None
                mergeList.append(self.mergedList(l1, l2))
            lists = mergeList
        return lists[0] if lists else None

    def mergedList(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        c1, c2 = l1 if l1 else None, l2 if l2 else None
        while c1 and c2:
            if c1.val < c2.val:
                cur.next = c1
                c1 = c1.next
            else:
                cur.next = c2
                c2 = c2.next
            cur = cur.next
        if c1:
            cur.next = c1
        if c2:
            cur.next = c2
        return dummy.next