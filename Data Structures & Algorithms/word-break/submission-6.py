class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
            for i in range(ind, len(s)):
                if s[ind: i + 1] in wordDict:
                    q.append(i + 1)

        return False

            