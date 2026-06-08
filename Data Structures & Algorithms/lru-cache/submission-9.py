class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(-1, 0)
        self.right = Node(-1, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {}

    def get(self, key: int) -> int:
        print(self.cache)
        if key in self.cache:
            node = self.cache[key]

            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev

            prev = self.right.prev
            prev.next = node
            node.prev = prev
            node.next = self.right
            self.right.prev = node
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            prev = node.prev
            next = node.next
            prev.next = next
            next.prev = prev
        else:
            node = Node(key, value)
            self.cache[key] = node

        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

        if len(self.cache) > self.capacity:
            temp = self.left.next
            self.left.next = temp.next
            temp.next.prev = self.left
            self.cache.pop(temp.key, None)



            

        

