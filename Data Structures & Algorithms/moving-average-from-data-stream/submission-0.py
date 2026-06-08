class MovingAverage:

    def __init__(self, size: int):
        self.total = 0
        self.size = size
        self.q = deque()

    def next(self, val: int) -> float:
        self.q.append(val)
        self.total += val
        avg = self.total / len(self.q)
        if len(self.q) == self.size:
            left = self.q.popleft()
            self.total -= left
        return avg


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
