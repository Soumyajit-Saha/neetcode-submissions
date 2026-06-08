class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        visited = set()

        while q:
            i = q.popleft()
            if i in visited:
                continue
            if i == len(s) - 1:
                return True
            for j in range(i + minJump, min(i + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    q.append(j)
            visited.add(i)

        return False