class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index = {}

        for i, c in enumerate(order):
            index[c] = i

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            minLen = min(len(word1), len(word2))
            if word1[: minLen] == word2[: minLen] and len(word1) > len(word2):
                return False
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    if index[word1[j]] > index[word2[j]]:
                        return False
                    break

        return True
