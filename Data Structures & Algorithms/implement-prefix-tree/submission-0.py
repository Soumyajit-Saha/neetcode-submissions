class PrefixTree:

    def __init__(self):
        self.children = defaultdict(PrefixTree)
        self.end = False

    def insert(self, word: str) -> None:
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = PrefixTree()
            root = root.children[w]

        root.end = True

    def search(self, word: str) -> bool:
        root = self
        for w in word:
            if w not in root.children:
                return False
            root = root.children[w]
        return root.end
        

    def startsWith(self, prefix: str) -> bool:
        root = self
        for w in prefix:
            if w not in root.children:
                return False
            root = root.children[w]
        return True
        