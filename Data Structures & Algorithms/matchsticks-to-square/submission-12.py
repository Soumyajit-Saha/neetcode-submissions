class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        target = sum(matchsticks) // 4

        visited = set()

        def dfs(start, nthside, sideSum):
            if nthside == 4:
                return True
            if sideSum == target:
                return dfs(0, nthside + 1, 0)
            for i in range(start, len(matchsticks)):
                if i in visited or sideSum + matchsticks[i] > target:
                    continue
                visited.add(i)
                if dfs(i + 1, nthside, sideSum + matchsticks[i]):
                    return True
                visited.remove(i)

                if start == 0:
                    break

            return False
            

        return dfs(0, 0, 0)
