class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.keyNodeMap = defaultdict(Node)
    
    def size(self):
        return len(self.keyNodeMap)

    def remove(self, key):
        if key in self.keyNodeMap:
            node = self.keyNodeMap[key]
            prev = node.prev
            next = node.next

            prev.next = next
            next.prev = prev
            self.keyNodeMap.pop(key, None)

    def popleft(self):
        node = self.left.next

        self.remove(node.key)
        return node.key

    def appendRight(self, key):
        node = Node(key)

        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.keyNodeMap[key] = node



class LFUCache:

    def __init__(self, capacity: int):
        self.keyValMap = {}
        self.capacity = capacity
        self.countLRUMap = defaultdict(LRUCache)
        self.keyCountMap = defaultdict(int)
        self.lfuCount = 0

    def get(self, key: int) -> int:
        if key not in self.keyValMap:
            return -1
        count = self.keyCountMap[key]
        self.countLRUMap[count].remove(key)

        self.countLRUMap[count + 1].appendRight(key)
        self.keyCountMap[key] = count + 1

        if self.countLRUMap[count].size() == 0 and self.lfuCount == count:
            self.lfuCount = count + 1

        return self.keyValMap[key]


    def put(self, key: int, value: int) -> None:
        if len(self.keyValMap) == self.capacity and key not in self.keyValMap:
            lfu = self.countLRUMap[self.lfuCount].popleft()
            self.keyValMap.pop(lfu, None)
            self.keyCountMap.pop(lfu, None)
        
        if key in self.keyValMap:
            count = self.keyCountMap[key]
            self.countLRUMap[count].remove(key)
        else:
            count = 0

        self.countLRUMap[count + 1].appendRight(key)
        self.keyCountMap[key] = count + 1
        self.keyValMap[key] = value

        if self.countLRUMap[count].size() == 0 and self.lfuCount == count:
            self.lfuCount = count + 1

        self.lfuCount = min(self.lfuCount, count + 1)
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)