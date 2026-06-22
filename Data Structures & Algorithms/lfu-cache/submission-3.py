from collections import defaultdict

class ListNode:
    def __init__(self, key, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.nodes = {}  # key -> node

    def length(self):
        return len(self.nodes)

    def append(self, key, val):
        node = ListNode(key, val)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.nodes[key] = node

    def remove(self, key):
        node = self.nodes.pop(key)
        node.prev.next = node.next
        node.next.prev = node.prev

    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.remove(node.key)
        return node.key, node.val


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.minFreq = 0
        self.valMap = {}              # key -> value
        self.countMap = {}            # key -> freq
        self.listMap = defaultdict(LinkedList)  # freq -> LinkedList of keys

    def _update(self, key):
        freq = self.countMap[key]
        self.listMap[freq].remove(key)

        if freq == self.minFreq and self.listMap[freq].length() == 0:
            self.minFreq += 1

        self.countMap[key] = freq + 1
        self.listMap[freq + 1].append(key, self.valMap[key])

    def get(self, key: int) -> int:
        if key not in self.valMap:
            return -1
        self._update(key)
        return self.valMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.valMap:
            self.valMap[key] = value
            self._update(key)
            return

        if self.size == self.cap:
            evict_key, _ = self.listMap[self.minFreq].popLeft()
            del self.valMap[evict_key]
            del self.countMap[evict_key]
            self.size -= 1

        self.valMap[key] = value
        self.countMap[key] = 1
        self.listMap[1].append(key, value)
        self.minFreq = 1
        self.size += 1