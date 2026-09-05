class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.end = True

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.addWord(word)
        

    def search(self, word: str) -> bool:
        def dfs(node, ind):
            if ind == len(word):
                return node.end
            if word[ind] in node.children:
                return dfs(node.children[word[ind]], ind + 1)
            else:
                if word[ind] == '.':
                    for child in node.children.values():
                        if dfs(child, ind + 1):
                            return True
                    return False
                else:
                    return False

        return dfs(self.root, 0)
                
        
