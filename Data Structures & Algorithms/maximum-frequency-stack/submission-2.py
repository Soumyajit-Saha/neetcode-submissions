class FreqStack:
    # Idea is to main a count map, that will store the count of each item
    # Then to know the max count we set a var for that.
    # There will also be a var stacks that stores count as key and all items that has that count
    # Now whenever a new count comes in, create a key with the count in stacks and append the item to the value list
    # 
    def __init__(self):
        self.stacks = {}
        self.count = {}
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.count[val] = self.count.get(val, 0) + 1
        if self.count[val] > self.maxCount:
            self.maxCount = self.count[val]
        if self.count[val] not in self.stacks:
            self.stacks[self.count[val]] = []
        self.stacks[self.count[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop()
        if not self.stacks[self.maxCount]:
            self.maxCount -= 1
        self.count[res] -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()