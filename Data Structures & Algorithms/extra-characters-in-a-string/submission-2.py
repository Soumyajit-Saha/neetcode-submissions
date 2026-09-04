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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        root = Trie()
        for word in dictionary:
            root.add(word)
        
        dp = {}
        def dfs(ind):
            if ind == len(s):
                return 0
            if ind in dp:
                return dp[ind]
            res = 1 + dfs(ind + 1)
            curr = root
            for i in range(ind, len(s)):
                if s[i] not in curr.children:
                    break
                curr = curr.children[s[i]]
                if curr.end:
                    res = min(res, dfs(i + 1))
            dp[ind] = res
            return dp[ind]

        return dfs(0)
        