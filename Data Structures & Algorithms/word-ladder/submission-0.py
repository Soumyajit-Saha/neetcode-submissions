class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patternMap = defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[: i] + "*"
                if i < len(word) - 1:
                    pattern = pattern + word[i + 1:]
                patternMap[pattern].append(word)

        visited = set()
        queue = deque()
        queue.append(beginWord)

        res = 1

        while queue:
            size = len(queue)
            for s in range(size):
                word = queue.popleft()
                if word in visited:
                    continue
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[: i] + "*"
                    if i < len(word) - 1:
                        pattern = pattern + word[i + 1:]

                    for nei in patternMap[pattern]:
                        queue.append(nei)
                visited.add(word)

            res += 1

        return 0
            