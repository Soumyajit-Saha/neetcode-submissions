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
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # The idea is to have recursive func that is called with an index of s
        # the func returns the minimum extra chars starting from that index
        # In the function, we first check min extra chars if we omit that index char
        # Then check min extra chars including the char at index
        # To check min extra chars including the char at index, we go through all possible words formed from index and add the func(end of word + 1) i.e. the min extra chars starting after end of word index
        # To find all possible words from index, we use trie
        # If there is not branch in trie that matches a substring starting index, we break from checking more

        root = Trie()
        for word in dictionary:
            root.add(word)

        dp = {}

        def dfs(i):
            if i == len(s):
                # When we go beyond the length, return 0. Base case
                return 0
            if i in dp:
                return dp[i]
            
            # first check the min extra chars when we omit the char at index
            res = 1 + dfs(i + 1)

            # Then check the min extra chars including the char at index
            curr = root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.end:
                    res = min(res, dfs(j + 1))
                
            dp[i] = res
            return dp[i]

        return dfs(0)
