class StockSpanner:

    def __init__(self):
        self.stack = []
        self.indStack = []
        self.currIndex = 0

    def next(self, price: int) -> int:
        ind = self.currIndex
        while self.stack and self.stack[-1] <= price:
            ind = self.indStack.pop()
            self.stack.pop()
        
        res = self.currIndex - ind + 1

        self.indStack.append(ind)
        self.stack.append(price)
        self.currIndex += 1

        return res
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)