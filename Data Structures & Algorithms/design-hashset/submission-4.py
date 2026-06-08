class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None
    
    def add(self, val, node):
        if not node:
            return Node(val)
        elif node.val > val:
            node.left = self.add(val, node.left)
        elif node.val < val:
            node.right = self.add(val, node.right)
        return node

    def search(self, val, node):
        if not node:
            return False
        elif node.val > val:
            return self.search(val, node.left)
        elif node.val < val:
            return self.search(val, node.right)
        else:
            return True

    def delete(self, val, node):
        if not node:
            return None
        elif node.val > val:
            node.left = self.delete(val, node.left)
        elif node.val < val:
            node.right = self.delete(val, node.right)
        else:
            if not node.left and not node.right:
                return None
            elif node.left and not node.right:
                return node.left
            elif not node.left and node.right:
                return node.right
            else:
                succ = node.right
                while succ.left:
                    succ = succ.left
                node.val = succ.val
                self.delete(succ.val, node.right)
        return node

                


class MyHashSet:

    def __init__(self):
        self.bst = BST()

    def add(self, key: int) -> None:
        self.bst.root = self.bst.add(key, self.bst.root)

    def remove(self, key: int) -> None:
        self.bst.root = self.bst.delete(key, self.bst.root)

    def contains(self, key: int) -> bool:
        return self.bst.search(key, self.bst.root)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)