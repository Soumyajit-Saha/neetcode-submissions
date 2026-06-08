class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0

        while q:
            i = q.popleft()
            if i == len(s) - 1:
                return True
            start = max(farthest, i + minJump)
            for j in range(start, min(i + maxJump, len(s) - 1) + 1):
                if s[j] == '0':
                    q.append(j)
            farthest = i + maxJump

        return False