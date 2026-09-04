class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.end = False

    def add(self, word):
        curr = self
        for w in word:
            if w not in curr.children:
                curr.children[w] = Trie()
            curr = curr.children[w]
        curr.end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        root = Trie()
        for word in wordDict:
            root.add(word)
        dp = {}

        def dfs(ind):
            if ind == len(s):
                return [""]
            if ind in dp:
                return dp[ind]
            sentences = []
            curr = root
            for i in range(ind, len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.end:
                    for next_sentence in dfs(i + 1):
                        if not next_sentence:
                            sentences.append(s[ind: i + 1])
                        else:
                            sentences.append(s[ind: i + 1] + ' ' + next_sentence)
            dp[ind] = sentences
            return dp[ind]

        return dfs(0)




