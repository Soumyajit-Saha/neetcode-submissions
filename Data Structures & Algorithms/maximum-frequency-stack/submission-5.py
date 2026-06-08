class FreqStack:

    def __init__(self):
        self.countStackMap = defaultdict(list)
        self.maxCount = 0
        self.countMap = {}

    def push(self, val: int) -> None:
        self.countMap[val] = self.countMap.get(val, 0) + 1
        self.countStackMap[self.countMap[val]].append(val)
        self.maxCount = max(self.maxCount, self.countMap[val])

    def pop(self) -> int:
        stack = self.countStackMap[self.maxCount]
        val = stack.pop()
        if len(stack) == 0:
            self.maxCount -= 1
        self.countMap[val] -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()