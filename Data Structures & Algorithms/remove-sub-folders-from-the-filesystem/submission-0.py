class Trie:
    def __init__(self, name=''):
        self.name = name
        self.children = {}
        self.end = False
    
    def add(self, path):
        path = [p for p in path.split('/') if p]
        curr = self
        for p in path:
            if p not in curr.children:
                curr.children[p] = Trie(p)
            curr = curr.children[p]
        curr.end = True


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for path in folder:
            root.add(path)
        res = []
        def dfs(node, path):
            if node.end:
                res.append(path)
                return
            for child in node.children.values():
                dfs(child, path + '/' + child.name)
        
        dfs(root, '')
        return res
