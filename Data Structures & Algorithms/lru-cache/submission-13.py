class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left
        self.keyValMap = {}
        self.keyNodeMap = defaultdict(Node)

    def get(self, key: int) -> int:
        if key not in self.keyValMap:
            return -1
        node = self.keyNodeMap[key]

        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

        return self.keyValMap[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.keyValMap and len(self.keyValMap) == self.capacity:
            node = self.left.next
            self.left.next = node.next
            node.next.prev = self.left
            self.keyValMap.pop(node.key, None)
            self.keyNodeMap.pop(node.key, None)
            del node

        if key in self.keyValMap:
            node = self.keyNodeMap[key]

            prev = node.prev
            next = node.next

            prev.next = next
            next.prev = prev

        else:
            node = Node(key)
            self.keyNodeMap[key] = node

        
        last = self.right.prev
        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

        self.keyValMap[key] = value
        
