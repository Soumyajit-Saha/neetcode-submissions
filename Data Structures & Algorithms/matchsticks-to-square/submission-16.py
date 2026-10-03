class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        visited = set()
        total = sum(matchsticks)
        if total % 4 != 0:
            return False
        matchsticks.sort()
        sideLen = total // 4

        def dfs(ind, side, sideSum):
            if side == 4:
                return True
            if sideSum == sideLen:
                return dfs(0, side + 1, 0)
            for i in range(ind, len(matchsticks)):
                if sideSum + matchsticks[i] > sideLen or i in visited:
                    continue
                visited.add(i)
                if dfs(i + 1, side, sideSum + matchsticks[i]):
                    visited.remove(i)
                    return True
                visited.remove(i)
                if ind == 0:
                    break
            return False

        return dfs(0, 0, 0)