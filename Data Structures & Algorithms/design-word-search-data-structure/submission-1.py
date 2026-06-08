class WordDictionary:

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.end = False

    def addWord(self, word: str) -> None:
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = WordDictionary()
            curr = curr.children[w]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self

        def dfs(start, curr):
            for i in range(start, len(word)):
                if word[i] != '.':
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
                else:
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                
            return curr.end

        return dfs(0, curr)

