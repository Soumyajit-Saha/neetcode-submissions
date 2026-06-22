class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        side = s // 4
        visited = set()
        matchsticks.sort(reverse=True)

        def dfs(start, subsetSum, nthSubset):
            if nthSubset == 4:
                return True
            if subsetSum == side:
                return dfs(0, 0, nthSubset + 1)
            for i in range(start, len(matchsticks)):
                if matchsticks[i] + subsetSum > s or i in visited:
                    continue
                visited.add(i)
                if dfs(i + 1, matchsticks[i] + subsetSum, nthSubset):
                    visited.remove(i)
                    return True
                visited.remove(i)

                if subsetSum == 0:
                    break
            return False

        return dfs(0, 0, 0)

                
