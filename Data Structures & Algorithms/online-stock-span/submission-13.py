class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        index = 1
        while self.stack and self.stack[-1][0] <= price:
            _, i = self.stack.pop()
            index += i
        self.stack.append([price, index])
        return index
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)