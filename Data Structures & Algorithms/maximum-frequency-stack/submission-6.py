class FreqStack:

    def __init__(self):
        self.countMap = {}
        self.stacks = {}
        self.maxFreq = 0

    def push(self, val: int) -> None:
        count = self.countMap.get(val, 0)

        if val in self.countMap:
            self.countMap[val] += 1
        else:
            self.countMap[val] = 1

        if count + 1 in self.stacks:
            self.stacks[count + 1].append(val)
        else:
            self.stacks[count + 1] = [val]

        self.maxFreq = max(count + 1, self.maxFreq)

    def pop(self) -> int:
        val = self.stacks[self.maxFreq].pop()
        if len(self.stacks[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.countMap[val] -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()