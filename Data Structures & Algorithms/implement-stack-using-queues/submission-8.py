class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        if self.q:
            return self.q.popleft()
        return -1
        

    def top(self) -> int:
        if self.q:
            return self.q[-1]
        return -1
        

    def empty(self) -> bool:
        return True if not self.q else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()