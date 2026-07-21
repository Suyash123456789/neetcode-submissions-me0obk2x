class ListNode:
    def __init__(self, val=0, prev=None, nxt=None):
        self.val = val
        self.prev = prev
        self.next = nxt


class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.size = 0

        self.left = ListNode()   # Front sentinel
        self.right = ListNode()  # Rear sentinel

        self.left.next = self.right
        self.right.prev = self.left

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        previous = self.right.prev
        node = ListNode(value, previous, self.right)

        previous.next = node
        self.right.prev = node

        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        first = self.left.next
        self.left.next = first.next
        first.next.prev = self.left

        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.next.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.prev.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity