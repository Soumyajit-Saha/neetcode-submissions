class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False

    def add(self, word):
        root = self
        for w in word:
            if w not in root.children:
                root.children[w] = Trie()
            root = root.children[w]
        root.end = True


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = Trie()
        for word in wordDict:
            root.add(word)

        dp = {}

        def dfs(start):
            if start == len(s):
                return [""]
            if start in dp:
                return dp[start]
            
            sentences = []
            curr = root
            for i in range(start, len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.end:
                    next_sentences = dfs(i + 1)
                    for next_sentence in next_sentences:
                        if next_sentence:
                            sentences.append(s[start: i + 1] + " " + next_sentence)
                        else:
                            sentences.append(s[start: i + 1])
            dp[start] = sentences
            return dp[start]

        return dfs(0)


            