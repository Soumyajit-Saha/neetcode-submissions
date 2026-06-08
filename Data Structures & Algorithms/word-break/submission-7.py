class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False

    def add(self, word):
        node = self
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
        node.end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie()
        for word in wordDict:
            root.add(word)

        visited = set()
        q = deque()
        q.append(0)

        while q:
            ind = q.popleft()
            if ind in visited:
                continue
            if ind == len(s):
                return True
            visited.add(ind)
            node = root
            for i in range(ind, len(s)):
                if s[i] not in node.children:
                    break
                node = node.children[s[i]]
                if node.end:
                    q.append(i + 1)

        return False

            