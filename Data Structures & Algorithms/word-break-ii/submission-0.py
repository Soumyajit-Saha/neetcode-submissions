class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        dp = {}

        def dfs(i):
            if i == len(s):
                # From this point we cannot return any list of sentences
                return [""]
            if i in dp:
                return dp[i]

            res = []
            for j in range(i, len(s)):
                word = s[i: j + 1]
                if word in wordDict:
                    nextSentences = dfs(j + 1)
                    for nextSentence in nextSentences:
                        # For each next sentences add the curr word to that
                        # And add these sentences to res
                        sentence = word
                        if nextSentence:
                            sentence += " " + nextSentence
                        res.append(sentence)
            
            dp[i] = res
            return dp[i]

        return dfs(0)