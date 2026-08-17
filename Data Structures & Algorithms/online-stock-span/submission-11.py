class StockSpanner:

    def __init__(self):
        self.stack = []
        
        

    def next(self, price: int) -> int:
        start = 1
        while self.stack and self.stack[-1][0] <= price:
            stock, index = self.stack.pop()
            start += index
        self.stack.append((price, start))
        return start
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)