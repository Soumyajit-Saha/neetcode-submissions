class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

# Will need to map the count to an LRU linked list
class LRUList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {} # stores key -> node map

    def length(self):
        return len(self.map)

    def remove(self, key):
        if key in self.map:
            node = self.map[key]
            prev = node.prev
            next = node.next

            prev.next = next
            next.prev = prev

            self.map.pop(key, None)

    def pushRight(self, key):
        node = Node(key)
        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node
        self.map[key] = node

    def popLeft(self):
        res = self.left.next
        self.remove(res.val)
        return res

class LFUCache:

    def __init__(self, capacity: int):
        self.countMap = defaultdict(int) # key -> count map
        self.capacity = capacity
        # since we store keys in nodes, which are in list for a count in list map, we need to store val for each key
        self.keyValMap = {} # key -> val map, 
        self.listMap = defaultdict(LRUList) # count -> LRU list map
        self.lfuCount = 0
        

    def get(self, key: int) -> int:
        if key not in self.keyValMap:
            return -1
        count = self.countMap[key]
        self.countMap[key] += 1

        self.listMap[count].remove(key)

        self.listMap[count + 1].pushRight(key)

        # LRU List for count is 0 and count was the least count
        if count == self.lfuCount and self.listMap[count].length() == 0:
            self.lfuCount += 1

        return self.keyValMap[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keyValMap and len(self.keyValMap) == self.capacity:
            res = self.listMap[self.lfuCount].popLeft()
            self.keyValMap.pop(res.val)
            self.countMap.pop(res.val)

        self.keyValMap[key] = value

        count = self.countMap[key]
        self.countMap[key] += 1

        self.listMap[count].remove(key)

        self.listMap[count + 1].pushRight(key)

        # LRU List for count is 0 and count was the least count
        if count == self.lfuCount and self.listMap[count].length() == 0:
            self.lfuCount += 1

        self.lfuCount = min(self.lfuCount, self.countMap[key])
    


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)