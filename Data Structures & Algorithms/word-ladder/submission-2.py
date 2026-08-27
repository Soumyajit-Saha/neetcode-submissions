class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternMap = {}

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1: ]
                if pattern in patternMap:
                    patternMap[pattern].append(word)
                else:
                    patternMap[pattern] = [word]


        q = deque()
        q.append([beginWord, 1])
        visited = set()

        while q:
            word, steps = q.popleft()
            if word == endWord:
                return steps
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1: ]
                for nei in patternMap.get(pattern, []):
                    if nei not in visited:
                        q.append([nei, steps + 1])

        return 0