class Trie:
    def __init__(self):
        self.children = {}
        self.end = False

    def add(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
               curr.children[w] = Trie()
            curr = curr.children[w]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = Trie()

        for word in words:
            root.add(word)

        visited = set()
        res = set()

        def dfs(i, j, word, node):

            if node.end:
                res.add(word)

            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or (i, j) in visited or board[i][j] not in node.children:
                return

            word += board[i][j]
            visited.add((i, j))

            node = node.children[board[i][j]]

            dfs(i + 1, j, word, node)
            dfs(i - 1, j, word, node)
            dfs(i, j + 1, word, node)
            dfs(i, j - 1, word, node)

            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, '', root)

        return list(res)


