class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key=key
        self.val=val
        self.next=next


class MyHashMap:
    def __init__(self):
        self.map=[ListNode() for i in range(1000)]
        
    def hash(self, key):
        return key%len(self.map)
    def put(self, key, value):
        cur=self.map[self.hash(key)]
        while cur.next:
            if cur.next.key==key:
                cur.next.val=value
                return
            cur=cur.next
        cur.next=ListNode(key, value)

        
        
    def get(self, key: int):
        cur=self.map[self.hash(key)]
        while cur:
            if cur.key==key:
                return cur.val
            cur=cur.next
        return -1
        
    def remove(self, key):
        cur=self.map[self.hash(key)]
        while cur and cur.next:
            if cur.next.key==key:
                cur.next=cur.next.next
                return
            cur=cur.next
        return
        