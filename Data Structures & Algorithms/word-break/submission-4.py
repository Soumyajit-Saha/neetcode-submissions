class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque()
        visited = set()
        queue.append(0)

        while queue:
            index = queue.popleft()
            if index in visited:
                continue
            if index == len(s):
                return True
            for word in wordDict:
                if index + len(word) - 1 < len(s) and s[index: index + len(word)] == word:
                    queue.append(index + len(word))
            visited.add(index)

        return False

