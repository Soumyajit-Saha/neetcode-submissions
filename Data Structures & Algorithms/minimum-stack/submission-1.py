class MinStack:

    def __init__(self):
        self.stack = []
        self.minAtIndex = []
        self.currMin = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.currMin > val:
            self.currMin = val
        self.minAtIndex.append(self.currMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minAtIndex.pop()
        self.currMin = self.minAtIndex[-1] if self.minAtIndex else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currMin
        
