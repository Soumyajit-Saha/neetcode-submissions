class StockSpanner:

    def __init__(self):
        self.stack = []
        self.indStack = []
        self.count = 0

    def next(self, price: int) -> int:
        ind = self.count
        while self.stack and self.stack[-1] <= price:
            ind = self.indStack.pop()
            self.stack.pop()
        
        res = self.count - ind + 1

        self.indStack.append(ind)
        self.stack.append(price)
        self.count += 1

        return res
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)