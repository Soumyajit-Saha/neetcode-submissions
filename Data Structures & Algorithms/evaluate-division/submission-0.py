class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for i in range(len(equations)):
            var1 = equations[i][0]
            var2 = equations[i][1]
            val = values[i]
            adjList[var1].append((var2, val))
            adjList[var2].append((var1, 1/val))

        visited = set()
        def dfs(var, target):
            if var not in adjList:
                return -1.0
            if var in visited:
                return -1.0
            if var == target:
                return 1
            visited.add(var)
            for nei, val in adjList[var]:
                restVal = dfs(nei, target)
                if restVal != -1.0:
                    visited.remove(var)
                    return val * restVal
            visited.remove(var)
            return -1.0

        res = []
        for q in queries:
            res.append(dfs(q[0], q[1]))

        return res