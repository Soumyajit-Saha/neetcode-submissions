class Node:
    def __init__(self, key, val, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = {key: Node(-1, -1) for key in range(1000)}

    def hash(self, key):
        return key % 1000

    def put(self, key: int, value: int) -> None:
        curr = self.map[self.hash(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next

        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        curr = self.map[self.hash(key)].next

        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1
        

    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)